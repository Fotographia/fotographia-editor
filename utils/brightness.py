from PIL import Image, ImageEnhance
import os


def brightness(path, value):
    img_in = Image.open(path)

    img = ImageEnhance.Brightness(img_in)

    if value == 0:
        bright = 0.8
    elif value == 1:
        bright = 1.2

    img_out = img.enhance(bright)

    os.remove(path)
    img_out.save(path)
