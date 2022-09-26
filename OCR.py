import numpy as np
import pytesseract
from pytesseract import Output
import cv2
import matplotlib.pyplot as plt

path = './images/white.png'
image = cv2.imread(path)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

texts = pytesseract.image_to_string(rgb_image, lang='kor+eng')
result = pytesseract.image_to_data(rgb_image, output_type=Output.DICT)#테서렉트에서 좌표값 뽑아옴.

print("--  text start  --")
print(texts)
print("--   text end   --")
print("--  info start  --")
print(result)
print("--   info end   --")

for i in range(0, len(result["text"])):
    x = result["left"][i]
    y = result["top"][i]

    w = result["width"][i]
    h = result["height"][i]
    text = result["text"][i]
    conf = int(result["conf"][i])
    if conf > 70:
        text = "".join([c if ord(c)<128 else "" for c in text]).strip()
        cv2.rectangle(rgb_image, (x,y), (x + w, y + h), (0,255, 0), 2)
        cv2.putText(rgb_image, text,(x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,200),2)
    
#cv2.imshow('custom window name', rgb_image)
#cv2.waitKey(1000)