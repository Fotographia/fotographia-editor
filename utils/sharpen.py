from PIL import Image
from PIL import ImageFilter
import os


def sharpen(path, value):
    image = Image.open(path)

    img = image.filter(ImageFilter.SHARPEN)

    if value == 0:
        pass
    elif value == 1:
        img = img.filter(ImageFilter.SHARPEN)

    os.remove(path)
    img.save(path)
