import pytesseract
import cv2
from pytesseract import Output

class Tesseract_Ocr():
        
    def __init__(self):
        str_i=""

    def Get_Ocr_Tesseract(self, screenshot):
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

        str_result = pytesseract.image_to_string(screenshot, lang='eng+kor')
        result = pytesseract.image_to_data(screenshot, output_type=Output.DICT) # 테서렉트에서 좌표값 뽑아옴
        return result, str_result
