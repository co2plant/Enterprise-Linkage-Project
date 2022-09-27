import os
import cv2 as cv
import pytesseract as tes
from pytesseract import Output
import numpy as np


path = './images/opencs.png'
img = cv.imread(path)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

texts = tes.image_to_string(img, lang='kor+eng')
result = tes.image_to_data(img, output_type=Output.DICT)

for i in range(0, len(result["text"])):
    x = result["left"][i]
    y = result["top"][i]

    w = result["width"][i]
    h = result["height"][i]
    text = result["text"][i]
    conf = int(result["conf"][i])
    if conf > 70:
        text = "".join([c if ord(c)<128 else "" for c in text]).strip()
        cv.rectangle(img, (x,y), (x + w, y + h), (0,255, 0), 2)
        cv.putText(img, text,(x,y-10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,200),2)

while(True):
    cv.imshow('custom window name', img)
    cv.namedWindow('frame2', flags=cv.WINDOW_GUI_NORMAL)
    cv.waitKey(1)

# 추가 내용 1 : 부분 번역 기능 사용시 번역한 내용을 구성하는 단어들로 자동 단어장을 만들어줌. -- 이것으로 학습 할 수 있게함.
# 추가 내용 2 : 일정시간 이상 텍스트에 마우스 오버 시 해당 단어의 사전적 의미를 알려줌
# 추가 내용 3 : 번역된 화면을 자동으로 pdf로 만들어주는 기능
