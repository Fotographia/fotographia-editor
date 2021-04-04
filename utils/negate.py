import os
import cv2


def negate(path):
    img = cv2.imread(path)

    img = cv2.bitwise_not(img)

    os.remove(path)
    cv2.imwrite(path, img)
