import cv2
import os


def rotate(path):
    img = cv2.imread(path)

    img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

    os.remove(path)
    cv2.imwrite(path, img)
