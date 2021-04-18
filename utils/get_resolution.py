import cv2


def get_resolution(path):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    resolution = {}
    resolution["height"], resolution["width"] = image.shape
    return resolution
