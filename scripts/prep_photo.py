#!/usr/bin/env python3
"""
Prepares an input portrait photo for clean monochrome ASCII conversion:
  1. Isolates subject from background using rembg (u2net session) or OpenCV contouring
  2. Applies CLAHE (contrast-limited adaptive histogram equalization) for face depth
  3. Bilateral-smooths skin noise while preserving sharp feature contours
  4. Differences of Gaussians to accentuate facial ridges (pupils, eyelids, jawline)
  5. Composites onto pure white canvas and crops square around upper portrait

Output: source-prepped.png (consumed by make_ascii_svg.py).
"""
import os
import sys
import cv2
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
INP = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "faris-profile.jpg")
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "..", "source-prepped.png")


def isolate_subject(pil_in):
    try:
        import rembg
        session = rembg.new_session("u2net")
        cut = rembg.remove(pil_in.convert("RGBA"), session=session)
        rgba = np.array(cut)
        return rgba
    except Exception as e:
        print(f"rembg notice: {e}, falling back to OpenCV alpha/contour mask.", file=sys.stderr)
        rgba = np.array(pil_in.convert("RGBA"))
        gray = cv2.cvtColor(rgba[:, :, :3], cv2.COLOR_RGB2GRAY)
        h, w = gray.shape
        mask = np.zeros((h, w), dtype=np.uint8)
        cv2.ellipse(mask, (w // 2, int(h * 0.45)), (int(w * 0.42), int(h * 0.45)), 0, 0, 360, 255, -1)
        rgba[:, :, 3] = cv2.GaussianBlur(mask, (21, 21), 11)
        return rgba


def prep(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.", file=sys.stderr)
        sys.exit(1)

    pil_in = Image.open(input_path)
    rgba = isolate_subject(pil_in)
    alpha = rgba[:, :, 3]

    ys, xs = np.where(alpha > 30)
    if len(xs) == 0 or len(ys) == 0:
        ys, xs = np.where(alpha >= 0)

    min_y, max_y = ys.min(), ys.max()
    min_x, max_x = xs.min(), xs.max()

    # Upper body crop (top 65% of subject height)
    portrait_h = int((max_y - min_y) * 0.65)
    cx = (min_x + max_x) // 2
    side = max(max_x - min_x, portrait_h) + 40

    canvas = np.full((side, side, 4), [255, 255, 255, 0], dtype=np.uint8)
    x0 = max(0, cx - side // 2)
    y0 = max(0, min_y - 20)
    crop_rgba = rgba[y0:y0 + side, x0:x0 + side]
    ch, cw = crop_rgba.shape[:2]
    canvas[:ch, :cw] = crop_rgba

    # CLAHE contrast enhancement
    gray = cv2.cvtColor(canvas[:, :, :3], cv2.COLOR_RGB2GRAY)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    equalized = clahe.apply(gray)

    # Bilateral smoothing
    bilateral = cv2.bilateralFilter(equalized, 9, 35, 9)

    # Edge enhancement (Difference of Gaussians)
    fine = cv2.GaussianBlur(bilateral, (0, 0), 1.2).astype(np.float32)
    coarse = cv2.GaussianBlur(bilateral, (0, 0), 5.0).astype(np.float32)
    edges = np.clip((coarse - fine) / 30.0, 0, 1)

    c_alpha = canvas[:, :, 3]
    mask = c_alpha > 50
    if np.any(mask):
        lo, hi = np.percentile(bilateral[mask], [2, 95])
        tone = np.clip((bilateral.astype(np.float32) - lo) / max(1.0, hi - lo), 0, 1)
    else:
        tone = bilateral.astype(np.float32) / 255.0

    prepped = np.clip(tone - 0.5 * edges, 0, 1) * 255.0

    # Composite onto white
    norm_alpha = c_alpha.astype(np.float32) / 255.0
    norm_alpha = cv2.GaussianBlur(norm_alpha, (0, 0), 1.0)
    final_gray = prepped * norm_alpha + 255.0 * (1.0 - norm_alpha)

    out_im = Image.fromarray(final_gray.astype(np.uint8), mode="L")
    out_im.save(output_path)
    print(f"Prepped photo written to {output_path} ({out_im.size})")


if __name__ == "__main__":
    prep(INP, OUT)
