import cv2
import os


def flip(path):
    img = cv2.imread(path)

    img = cv2.flip(img, 0)

    os.remove(path)
    cv2.imwrite(path, img)
