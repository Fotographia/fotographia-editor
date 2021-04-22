import cv2
import os


def water_color(path, wc_value):
    img = cv2.imread(path)

    res = cv2.stylization(img, sigma_s=60, sigma_r=wc_value)

    os.remove(path)
    cv2.imwrite(path, res)
