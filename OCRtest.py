import pytesseract
import cv2
import matplotlib.pyplot as plt

# Author : co2plant
# /opt/homebrew/Cellar/tesseract/5.2.0/share 
# tesseract testdata path in Mac

path = './images/test_kor_eng.png'
image = cv2.imread(path)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

text = pytesseract.image_to_string(rgb_image, lang='kor+eng')
print("--")
print(text)
print("--")