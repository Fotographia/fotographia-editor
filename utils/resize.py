import cv2
import os


def resize(path, width, height):
    img = cv2.imread(path)

    img = cv2.resize(img, (width, height))

    os.remove(path)
    cv2.imwrite(path, img)
