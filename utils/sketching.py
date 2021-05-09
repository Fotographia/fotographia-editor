import cv2
import os


def sketching(path, mode, sr, sf):
    img = cv2.imread(path)

    dst_gray, dst_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=sr, shade_factor=sf)

    if mode == 0:
        res = dst_gray
    elif mode == 1:
        res = dst_color

    os.remove(path)
    cv2.imwrite(path, res)
