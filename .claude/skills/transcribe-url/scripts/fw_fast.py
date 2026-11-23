"""fw_fast.py: one fast faster-whisper call for every script here that transcribes.

    segments, info, device = fw_fast.transcribe(audio_path, "small.en", word_timestamps=False, verbatim=False)
    segments -> [{"start", "end", "text", "words": [{"start", "end", "word"}]}]
    info     -> {"language", "language_probability", "duration"}

It picks the fastest lane this machine has, in this order, and runs faster-whisper's batched
pipeline on it:

    NVIDIA GPU (cuda)  ->  Apple Silicon GPU (mps)  ->  CPU (every machine)

Each lane runs in its own child process, so a lane that fails to load, runs out of memory or
crashes outright (a missing cuDNN aborts the process, it does not raise) just hands the job to
the next lane. A broken GPU stack can make a transcript slower; it can never block one.

AMD and Intel GPUs have no lane: ctranslate2, the engine under faster-whisper, has no backend
for them. Those machines take the CPU lane, which is still batched.

WHISPER_DEVICE=cpu|mps|cuda forces a lane (the CPU stays as the fallback).

verbatim=True (or WHISPER_VERBATIM=1) trades speed for the speaker's exact words. The batched
pipeline decodes each 30 s window on its own, and Whisper then tidies speech: on a 3-minute
reel it kept 25 of 35 spoken "like"s. Verbatim decodes in order with beam 5, each window seeing
the text before it, and kept 34. Still on the GPU: 6 s against the batched 2.3 s (old CPU call:
21 s). Use it where the wording IS the product (the voice corpus); summaries don't need it.

Measured 2026-11-22 on a 20-minute reel, small.en, M5 Ultra: the old call (CPU, beam 5,
sequential) 146 s; this on the Apple GPU 10 s; this on the CPU 31 s. large-v3 on the GPU: 26 s.

THIS FILE IS COPIED, byte for byte, into every skill that transcribes, so each skill still works
on its own: transcribe-url, auto-poster, yt-description, voice-corpus-builder,
ig-competitor-research. Edit the transcribe-url copy, then copy it over the other four
(packaging/package-for-client.sh refuses to build when they differ).
"""
import glob
import json
import os
import shutil
import subprocess
import sys
import tempfile


def _log(msg):
    print(f"[whisper] {msg}", file=sys.stderr)


def _nvidia_dirs():
    """Where pip's nvidia-* wheels keep their libraries inside this venv."""
    import site
    sub = "bin" if os.name == "nt" else "lib"
    return [d for sp in site.getsitepackages() for d in glob.glob(os.path.join(sp, "nvidia", "*", sub))]


def _expose_nvidia():
    import ctypes
    for d in _nvidia_dirs():
        if os.name == "nt":
            os.add_dll_directory(d)
            os.environ["PATH"] = d + os.pathsep + os.environ.get("PATH", "")
        else:
            for _ in (1, 2):  # twice: the cuDNN parts depend on each other
                for so in sorted(glob.glob(os.path.join(d, "lib*.so.*"))):
                    try:
                        ctypes.CDLL(so, mode=ctypes.RTLD_GLOBAL)
                    except OSError:
                        pass


def _cuda_libs_load():
    import ctypes
    names = ("cublas64_12.dll", "cudnn64_9.dll") if os.name == "nt" else ("libcublas.so.12", "libcudnn.so.9")
    try:
        for n in names:
            ctypes.CDLL(n)
        return True
    except OSError:
        return False


def _cuda_ready():
    """The CUDA lane needs cuBLAS 12 + cuDNN 9. Use the system's, else this venv's pip wheels,
    else install those wheels once (.cuda-tried stops a failed install repeating every run)."""
    if _cuda_libs_load():
        return True
    _expose_nvidia()
    if _cuda_libs_load():
        return True
    tried = os.path.join(sys.prefix, ".cuda-tried")
    uv = shutil.which("uv")
    if os.path.exists(tried) or not uv:
        return False
    open(tried, "w").close()
    _log("NVIDIA GPU found: installing its speech libraries (cuBLAS + cuDNN, about 1.2 GB, one time)")
    subprocess.run([uv, "pip", "install", "--python", sys.executable,
                    "nvidia-cublas-cu12", "nvidia-cudnn-cu12>=9,<10"], stdout=sys.stderr, check=False)
    _expose_nvidia()
    if _cuda_libs_load():
        return True
    _log(f"the NVIDIA libraries did not load, so this machine transcribes on the CPU (retry: delete {tried})")
    return False


def lanes():
    """[(device, compute_type), ...] fastest first; the CPU is always last."""
    import ctranslate2
    forced = os.environ.get("WHISPER_DEVICE", "").strip().lower()
    out = []
    if forced in ("", "cuda"):
        try:
            if ctranslate2.get_cuda_device_count() > 0 and _cuda_ready():
                out += [("cuda", "float16"), ("cuda", "int8_float16")]  # the second fits 4 GB cards
        except Exception:
            pass
    if forced in ("", "mps"):
        try:  # ctranslate2 >= 4.9
            if getattr(ctranslate2, "get_mps_device_count", lambda: 0)() > 0:
                out.append(("mps", "float16"))
        except Exception:
            pass
    return out + [("cpu", "int8")]


def transcribe(audio, model_name, word_timestamps=False, verbatim=False):
    verbatim = verbatim or os.environ.get("WHISPER_VERBATIM", "") == "1"
    ladder = lanes()
    fd, result = tempfile.mkstemp(suffix=".json", prefix="fw-fast-")
    os.close(fd)
    try:
        for i, (device, compute) in enumerate(ladder):
            _log(f"model={model_name} lane={device}{' verbatim' if verbatim else ''}")
            rc = subprocess.run([sys.executable, os.path.abspath(__file__), "--worker", audio, model_name,
                                 device, compute, "1" if word_timestamps else "0",
                                 "1" if verbatim else "0", result]).returncode
            if rc == 0:
                with open(result, encoding="utf-8") as f:
                    data = json.load(f)
                return data["segments"], data["info"], device
            if i == len(ladder) - 1:
                raise RuntimeError(f"transcription failed on the {device} lane (exit {rc}); the error is above")
            _log(f"the {device} lane failed (exit {rc}); trying {ladder[i + 1][0]}")
    finally:
        try:
            os.remove(result)
        except OSError:
            pass


def _worker(audio, model_name, device, compute, words, verbatim, result):
    import logging
    import ctranslate2
    from faster_whisper import WhisperModel
    ctranslate2.set_log_level(logging.ERROR)  # hush the "MPS backend is experimental" banner
    if device == "cuda":
        _expose_nvidia()
    kw = dict(device=device, compute_type=compute)
    if device == "cpu":
        kw["cpu_threads"] = max(4, min(16, (os.cpu_count() or 8) // 2))
    try:  # a cached model skips the Hugging Face round trip
        model = WhisperModel(model_name, local_files_only=True, **kw)
    except Exception:
        model = WhisperModel(model_name, **kw)
    opts = dict(vad_filter=True, vad_parameters=dict(min_silence_duration_ms=500), word_timestamps=words == "1")
    try:
        from faster_whisper import BatchedInferencePipeline
    except ImportError:  # faster-whisper < 1.1 has no batched pipeline
        BatchedInferencePipeline = None
    if verbatim == "1" or BatchedInferencePipeline is None:
        segs, info = model.transcribe(audio, beam_size=5 if verbatim == "1" else 1, **opts)
    else:  # without_timestamps=False keeps sentence-sized segments instead of one per 30 s chunk
        segs, info = BatchedInferencePipeline(model=model).transcribe(
            audio, batch_size=16, beam_size=1, without_timestamps=False, **opts)
    out = [{"start": s.start, "end": s.end, "text": s.text.strip(),
            "words": [{"start": w.start, "end": w.end, "word": w.word.strip()} for w in (s.words or [])]}
           for s in segs]
    out = [s for s in out if s["text"]]
    with open(result, "w", encoding="utf-8") as f:
        json.dump({"segments": out, "info": {"language": info.language,
                   "language_probability": info.language_probability, "duration": info.duration}}, f)


if __name__ == "__main__":
    if len(sys.argv) == 9 and sys.argv[1] == "--worker":
        _worker(*sys.argv[2:])
    else:
        print("\n".join(f"{d} {c}" for d, c in lanes()))  # `python fw_fast.py` = show this machine's lanes
