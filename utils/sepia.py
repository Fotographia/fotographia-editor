import cv2
import os


def sepia(path):
    img = cv2.imread(path)

    # get image shape
    i, j, k = img.shape
    for x in range(i):
        # change image colors
        for y in range(j):
            R = img[x, y, 2] * 0.393 + img[x, y, 1] * 0.769 + img[x, y, 0] * 0.189
            G = img[x, y, 2] * 0.349 + img[x, y, 1] * 0.686 + img[x, y, 0] * 0.168
            B = img[x, y, 2] * 0.272 + img[x, y, 1] * 0.534 + img[x, y, 0] * 0.131
            if R > 255:
                img[x, y, 2] = 255
            else:
                img[x, y, 2] = R
            if G > 255:
                img[x, y, 1] = 255
            else:
                img[x, y, 1] = G
            if B > 255:
                img[x, y, 0] = 255
            else:
                img[x, y, 0] = B
    os.remove(path)
    cv2.imwrite(path, img)
