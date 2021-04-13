import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.image import imsave
import os


def edge_detection(path, select_val):

    img = cv2.imread(path, 0)
    val = int(select_val)

    if val == 0:
        result = cv2.Laplacian(img, cv2.CV_64F)
    elif val == 1:
        result = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
    elif val == 2:
        result = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

    os.remove(path)
    cv2.imwrite(path, result)
