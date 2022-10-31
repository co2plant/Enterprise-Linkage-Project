import numpy as np
import pytesseract
import cv2
import matplotlib.pyplot as plt
import overlay

from pytesseract import Output
from overlay import Overlay


class Tesseract_Ocr():
        
    def __init__(self):
        str_i=""

    def Get_Ocr_Tesseract(self, screenshot):
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

        text = pytesseract.image_to_string(screenshot, lang='eng+kor')
        result = pytesseract.image_to_data(screenshot, output_type=Output.DICT) # 테서렉트에서 좌표값 뽑아옴
        print(result)
        self.str_i = text
        return result

    def Get_Ocr_String(self):
        return self.str_i
