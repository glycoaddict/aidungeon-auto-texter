import cv2
import pytesseract

from PIL import Image
from glob import glob
import os
import re

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# POPPLER_PATH = 'poppler/poppler-/bin/'

f = 'img/scr2.png'

config = ("-l eng --oem 1 --psm 11")
im = Image.open(f)
text = pytesseract.image_to_string(im, config=config)
print(text)
