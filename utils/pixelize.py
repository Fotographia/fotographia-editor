from PIL import Image
import os


def pixelize(path, value):

    img = Image.open(path)

    # Resize smoothly down to x pixels
    imgSmall = img.resize((value, value), resample=Image.BILINEAR)

    # Scale back up using NEAREST to original size
    result = imgSmall.resize(img.size, Image.NEAREST)

    os.remove(path)
    result.save(path)
