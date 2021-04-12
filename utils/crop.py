import cv2
import os


def crop(path, X, Y, xOffset, yOffset):

    img = cv2.imread(path)
    y, x, _ = img.shape

    xNew = X + xOffset
    yNew = Y + yOffset
    if (X + xOffset) > x:
        xOffset -= xNew - x
    if (Y + yOffset) > y:
        yOffset -= yNew - y
    if X > x or Y > y:
        ...
    else:
        img = img[yOffset : Y + yOffset, xOffset : X + xOffset]

    os.remove(path)
    cv2.imwrite(path, img)
