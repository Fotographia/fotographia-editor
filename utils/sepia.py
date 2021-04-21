import numpy as np
import cv2
import os


def sepia(path):
    img = cv2.imread(path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    normalized_gray = np.array(gray, np.float32) / 255

    # solid color
    sepia = np.ones(img.shape)
    sepia[:, :, 0] *= 153  # B
    sepia[:, :, 1] *= 204  # G
    sepia[:, :, 2] *= 255  # R

    # hadamard
    sepia[:, :, 0] *= normalized_gray  # B
    sepia[:, :, 1] *= normalized_gray  # G
    sepia[:, :, 2] *= normalized_gray  # R

    img = np.array(sepia, np.uint8)

    os.remove(path)
    cv2.imwrite(path, img)
