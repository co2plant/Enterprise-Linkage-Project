import numpy as np
import pytesseract
import cv2
import matplotlib.pyplot as plt
import overlay

from pytesseract import Output


class Tesseract_Ocr:
        
    def Get_Ocr_Tesseract(self, screenshot):

        text = pytesseract.image_to_string(screenshot, lang='eng+kor')
        result_text = pytesseract.image_to_data(screenshot, output_type=Output.DICT) # 테서렉트에서 좌표값 뽑아옴
        
        return result_text
        