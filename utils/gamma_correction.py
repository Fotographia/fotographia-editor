import cv2
import numpy as np


def gamma_correction(path, gamma_value):
    image = cv2.imread(path).astype(np.float32) / 255

    # set value for gamma correction, place holder from 0.1-1.0
    gamma = gamma_value
    gamma_correction = np.power(image, gamma)

    cv2.imwrite(path, gamma_correction * 255)
