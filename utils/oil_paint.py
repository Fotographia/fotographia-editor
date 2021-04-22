import cv2
import os


def oil_paint(path, oil_level):
    img = cv2.imread(path)

    oil_intense = int(oil_level)
    res = cv2.xphoto.oilPainting(img, 5, oil_intense)

    os.remove(path)
    cv2.imwrite(path, res)
