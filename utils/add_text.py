from PIL import ImageFont, Image, ImageDraw
import os


def add_text(path, ftext, x, y, ffamily, fstyle, fcolor, fsize, falign):
    # Form font path to generate font family and style
    f = "static/fonts/prefix-style.ttf"
    f = f.replace("prefix", ffamily)
    f = f.replace("style", fstyle)

    img = Image.open(path)
    res = ImageDraw.Draw(img)

    # Set size and create font
    font = ImageFont.truetype(f, fsize)
    ftext = ftext.replace(r"\n", "\n")
    # Add text and its position, color and align
    res.text((x, y), ftext, fill=fcolor, font=font, align=falign)

    os.remove(path)
    img.save(path)
