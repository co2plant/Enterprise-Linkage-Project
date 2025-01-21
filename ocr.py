import pytesseract
import cv2
from pytesseract import Output
import os

class Tesseract_Ocr:
    def __init__(self):
        self.tesseract_cmd = os.getenv('TESSERACT_CMD', r'C:\Program Files\Tesseract-OCR\tesseract.exe')
        pytesseract.pytesseract.tesseract_cmd = self.tesseract_cmd

    def get_ocr_tesseract(self, screenshot):
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
        str_result = pytesseract.image_to_string(screenshot, lang='eng+kor')
        result = pytesseract.image_to_data(screenshot, output_type=Output.DICT)
        print(result)
        return result, str_result
