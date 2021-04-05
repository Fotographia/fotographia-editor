import numpy as np
import cv2 as cv
from PIL import Image
import os


def blur(path):
    image = Image.open(path)

    # convert image to numpy array
    img = np.array(image)

    # implement Gaussian blur on image
    blur = cv.GaussianBlur(img, (5, 5), 0)
    os.remove(path)
    blur = Image.fromarray(blur)
    blur.save(path)
