import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

ext_1 = os.path.splitext(sys.argv[1])[1]
ext_2 = os.path.splitext(sys.argv[2])[1]

if ext_1.lower() not in (".jpg",".jpeg",".png") or ext_2.lower() not in (".jpg",".jpeg",".png"):
    sys.exit("Invalid output")

if ext_1 != ext_2:
    sys.exit("Input and output have different extensions")

try:
    with open(sys.argv[1], "r") as file:
        pass
except FileNotFoundError:
    sys.exit("Input does not exist")


shirt = Image.open("shirt.png")
im = Image.open(sys.argv[1])
#print(im.format, im.size, im.mode)
muppet = ImageOps.fit(im,shirt.size)
muppet.paste(shirt, mask=shirt)
muppet.save(sys.argv[2])
