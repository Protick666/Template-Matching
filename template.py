import numpy
import math
from PIL import Image

im = Image.open('test.jpg') # Can be many different formats.
pix = im.load()
print (im.size )  # Get the width and hight of the image for iterating over
print (pix[256,1][0])  # Get the RGBA Value of the a pixel of an image



