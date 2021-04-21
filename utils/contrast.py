from PIL import Image, ImageEnhance
import os


def contrast(path, value):
    img = Image.open(path)

    # image brightness enhancer
    enhancer = ImageEnhance.Contrast(img)

    # decrease constrast
    if value == 0:
        factor = 0.5
    # increase contrast
    elif value == 1:
        factor = 1.5

    im_output = enhancer.enhance(factor)

    os.remove(path)
    im_output.save(path)
