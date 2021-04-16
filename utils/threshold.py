import cv2
import os


def threshold(path, values):

    img = cv2.imread(path, 0)
    thres_value = int(values)

    if thres_value == 0:
        ret, thres = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    elif thres_value == 1:
        thres = cv2.adaptiveThreshold(
            img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
        )
    elif thres_value == 2:
        thres = cv2.adaptiveThreshold(
            img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
        )

    os.remove(path)
    cv2.imwrite(path, thres)
