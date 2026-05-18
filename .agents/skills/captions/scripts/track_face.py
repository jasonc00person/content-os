#!/usr/bin/env python3
"""
track_face.py — sample face detections across a video and emit a chin-Y
trajectory for the captions skill to position lines below the chin.

Reuses the BlazeFace tflite from the reframe skill (no model duplication).

Usage:
    track_face.py <input_video> <out.json>

Output JSON:
{
  "fps": 30.0,
  "src_w": 1080,
  "src_h": 1920,
  "samples": [{"t": 0.000, "chin_y": 1124.3}, ...]
}

chin_y is the bottom edge of the face bounding box in pixels (top-left origin).
Samples are EMA-smoothed. Frames with no detection inherit the last known value.
"""
import json
import os
import sys
import cv2
import numpy as np

# --- Tunables -----------------------------------------------------
EMA_ALPHA = 0.20
SAMPLE_EVERY_N_FRAMES = 5
MIN_CONFIDENCE = 0.5
# ------------------------------------------------------------------

MODEL_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "reframe", "scripts", "face_detector.tflite",
)


def main():
    if len(sys.argv) != 3:
        sys.stderr.write("usage: track_face.py <input_video> <out.json>\n")
        sys.exit(1)

    src = sys.argv[1]
    out_path = sys.argv[2]

    if not os.path.exists(MODEL_PATH):
        sys.stderr.write(f"face_detector.tflite not found at {MODEL_PATH}\n")
        sys.exit(1)

    cap = cv2.VideoCapture(src)
    if not cap.isOpened():
        sys.stderr.write(f"cannot open {src}\n")
        sys.exit(1)
    src_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    src_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0

    from mediapipe.tasks import python as mp_python
    from mediapipe.tasks.python import vision
    import mediapipe as mp

    options = vision.FaceDetectorOptions(
        base_options=mp_python.BaseOptions(model_asset_path=MODEL_PATH),
        min_detection_confidence=MIN_CONFIDENCE,
    )
    detector = vision.FaceDetector.create_from_options(options)

    samples = []
    last_known = None
    ema_value = None
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
                biggest = max(
                    res.detections,
                    key=lambda d: d.bounding_box.width * d.bounding_box.height,
                )
                bb = biggest.bounding_box
                chin_y = float(bb.origin_y + bb.height)
                last_known = chin_y
            value = last_known
            if value is not None:
                ema_value = value if ema_value is None else EMA_ALPHA * value + (1 - EMA_ALPHA) * ema_value
                samples.append({"t": round(frame_idx / fps, 3), "chin_y": round(ema_value, 1)})
        frame_idx += 1

    cap.release()

    if not samples:
        sys.stderr.write("[track_face] no face detected in any sampled frame\n")
        sys.exit(2)

    out = {
        "fps": fps,
        "src_w": src_w,
        "src_h": src_h,
        "samples": samples,
    }
    with open(out_path, "w") as f:
        json.dump(out, f)
    ys = [s["chin_y"] for s in samples]
    sys.stderr.write(
        f"[track_face] {len(samples)} samples, chin_y range {min(ys):.0f}-{max(ys):.0f}px → {out_path}\n"
    )


if __name__ == "__main__":
    main()
