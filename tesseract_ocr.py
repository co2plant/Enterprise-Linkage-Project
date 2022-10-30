import numpy as np
import pytesseract
import cv2
import matplotlib.pyplot as plt
import overlay

from pytesseract import Output


class Tesseract_Ocr:
        
    def Get_Ocr_Tesseract(self, screenshot):
        rgb_image = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)

        text = pytesseract.image_to_string(rgb_image, lang='kor+eng')
        result_text = pytesseract.image_to_data(rgb_image, output_type=Output.DICT) # 테서렉트에서 좌표값 뽑아옴
        
        
        return result_text
        