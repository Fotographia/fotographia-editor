from PIL import Image
from PIL import ImageFilter
import os


def smooth(path, value):
    image = Image.open(path)

    img = image.filter(ImageFilter.SMOOTH)

    if value == 0:
        pass
    elif value == 1:
        img = image.filter(ImageFilter.SMOOTH_MORE)
    elif value == 2:
        img = img.filter(ImageFilter.SMOOTH)

    os.remove(path)
    img.save(path)
