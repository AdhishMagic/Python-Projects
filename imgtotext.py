import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe' #install OCR and set the path using [https://github.com/UB-Mannheim/tesseract/wiki]

def convert():
    img = Image.open('src/img.webp')
    text = pytesseract.image_to_string(img, lang='eng')
    print(text)

if __name__ == "__main__":
    convert()