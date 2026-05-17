#!/usr/bin/env python3
"""
reframe.py — face-tracked crop trajectory generator.

Reads a video, runs MediaPipe BlazeFace (Tasks API) per frame, EMA-smooths the
face center X, and writes a FFmpeg `sendcmd` file with `crop x` commands.

Usage:
    reframe.py <input_video> <out_cmd_file>

Prints to stdout for shell eval:
    CROP_W=<width>
    CROP_H=<height>
    SRC_W=<width>
    SRC_H=<height>
"""
import os
import sys
import cv2
import numpy as np

# --- Tunable constants -------------------------------------------------------
EMA_ALPHA = 0.15
SAMPLE_EVERY_N_FRAMES = 5
MIN_CONFIDENCE = 0.5
# ----------------------------------------------------------------------------

MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "face_detector.tflite")


def main():
    if len(sys.argv) != 3:
        sys.stderr.write("usage: reframe.py <input_video> <out_cmd_file>\n")
        sys.exit(1)

    src = sys.argv[1]
    cmd_path = sys.argv[2]

    cap = cv2.VideoCapture(src)
    if not cap.isOpened():
        sys.stderr.write(f"cannot open {src}\n")
        sys.exit(1)

    src_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    src_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    crop_h = src_h
    crop_w = int(round(src_h * 9 / 16))
    if crop_w > src_w:
        crop_w = src_w

    sys.stderr.write(f"[reframe] src {src_w}x{src_h} @ {fps:.2f}fps, {n_frames} frames\n")
    sys.stderr.write(f"[reframe] crop window {crop_w}x{crop_h}\n")

    from mediapipe.tasks import python as mp_python
    from mediapipe.tasks.python import vision
    import mediapipe as mp

    base_options = mp_python.BaseOptions(model_asset_path=MODEL_PATH)
    options = vision.FaceDetectorOptions(
        base_options=base_options,
        min_detection_confidence=MIN_CONFIDENCE,
    )
    detector = vision.FaceDetector.create_from_options(options)

    raw_x = []
    last_known = src_w / 2.0
    sample_indices = []

    frame_idx = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_idx % SAMPLE_EVERY_N_FRAMES == 0:
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
            res = detector.detect(mp_image)
            if res.detections:
                # Largest face by bbox area
                biggest = max(
                    res.detections,
                    key=lambda d: d.bounding_box.width * d.bounding_box.height,
                )
                bb = biggest.bounding_box
                fx = bb.origin_x + bb.width / 2
                last_known = float(fx)
            raw_x.append(last_known)
            sample_indices.append(frame_idx)
        frame_idx += 1
    cap.release()

    if not raw_x:
        sys.stderr.write("[reframe] no frames sampled; cannot build trajectory\n")
        sys.exit(1)

    smoothed = np.zeros(len(raw_x))
    smoothed[0] = raw_x[0]
    for i in range(1, len(raw_x)):
        smoothed[i] = EMA_ALPHA * raw_x[i] + (1 - EMA_ALPHA) * smoothed[i - 1]

    x_max = src_w - crop_w
    with open(cmd_path, "w") as f:
        for sample_i, frame_i in enumerate(sample_indices):
            t = frame_i / fps
            cx = int(round(smoothed[sample_i] - crop_w / 2))
            cx = max(0, min(x_max, cx))
            f.write(f"{t:.4f} crop x {cx};\n")

    sys.stderr.write(f"[reframe] wrote {len(sample_indices)} commands → {cmd_path}\n")
    print(f"CROP_W={crop_w}")
    print(f"CROP_H={crop_h}")
    print(f"SRC_W={src_w}")
    print(f"SRC_H={src_h}")


if __name__ == "__main__":
    main()
