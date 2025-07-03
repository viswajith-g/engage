#!/usr/bin/env python3
"""
grabcut_bg.py

Remove background using OpenCV's GrabCut algorithm.

Usage:
    python grabcut_bg.py input.jpg output.png
"""
import sys
import numpy as np
import cv2

base_path = "../images/"
input = "finance-software"
extension = ".png"
output = ""

def remove_background_grabcut(img_path: str, out_path: str):
    img = cv2.imread(img_path)
    h, w = img.shape[:2]

    # 1) Run GrabCut
    mask = np.zeros((h, w), np.uint8)
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)
    rect = (10, 10, w - 20, h - 20)
    cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

    # 2) Create a binary mask where sure- or probable-foreground=1, else=0
    mask2 = np.where((mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD), 1, 0).astype('uint8')

    # 3) Split original into B, G, R channels
    b, g, r = cv2.split(img)

    # 4) Create alpha channel from mask2 (0 or 255)
    alpha = (mask2 * 255).astype('uint8')

    # 5) Merge B,G,R and alpha into a 4-channel image
    rgba = cv2.merge([b, g, r, alpha])

    # 6) Write out as PNG (which supports alpha)
    cv2.imwrite(out_path, rgba)

if __name__ == "__main__":
    remove_background_grabcut(base_path+input+extension, base_path+input+output+extension)
