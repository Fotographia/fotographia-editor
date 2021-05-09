from PIL import ImageFilter
from PIL import Image
import os


def emboss(path, sel_depth, scale, offset):
    img = Image.open(path).convert("L")

    if sel_depth == 0:
        ImageFilter.EMBOSS.filterargs = (
            (3, 3),
            scale,
            offset,
            (-1, 0, 0, 0, 1, 0, 0, 0, 0),
        )
    elif sel_depth == 1:
        ImageFilter.EMBOSS.filterargs = (
            (3, 3),
            scale,
            offset,
            (-1, 0, 0, 0, 0, 0, 0, 0, 1),
        )

    im_emb = img.filter(ImageFilter.EMBOSS)

    os.remove(path)
    im_emb.save(path)
