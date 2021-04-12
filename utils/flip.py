import cv2
import os


def flip(path, select_val):
    img = cv2.imread(path)

    img = cv2.flip(img, int(select_val))

    os.remove(path)
    cv2.imwrite(path, img)
