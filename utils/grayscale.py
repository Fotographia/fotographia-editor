import cv2
import os


def grayscale(path):
    img = cv2.imread(path)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    os.remove(path)
    cv2.imwrite(path, img)