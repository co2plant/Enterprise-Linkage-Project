from platform import java_ver
from unittest import runner
from xml.etree.ElementTree import tostring
import cv2 as cv

import numpy as np
import os
import pytesseract
import matplotlib.pyplot as plt
import time
import tkinter

from asyncio.windows_events import NULL
from hashlib import new
from overlay import Overlay
from capture import Capture
from ocr import Tesseract_Ocr
import translate
#--------------------------------------------------------------------

os.chdir(os.path.dirname(os.path.abspath(__file__)))

Capture.list_window_names()
window_name=input()

caps = Capture(window_name)
ocrs = Tesseract_Ocr()

looptime = time.time()

#------------------------------variable------------------------------
global overlay_screen_1
global overlay_screen_2
array = []
#--------------------------------------------------------------------

#--------------------------------------------------------------------

def button1_pressed():
    if 'overlay_screen' in globals():
        overlay_screen.stop()
        del overlay_screen
    else:
        overlay_screen = Overlay(frame1)

#--------------------------------------------------------------------

#--------------------------------------------------------------------

def while_loop():
    screenshot = caps.get_screenshot()
    result, str_result = ocrs.Get_Ocr_Tesseract(screenshot)
    minimum_left=10000
    minimum_top=10000
    
    for i in range(1, len(result["text"])):
        text = result["text"][i]
        conf = int(result["conf"][i])
        arr=caps.get_rect()#arr[0] = x, arr[1]=y
        
    
        if(conf>70 and ((result["left"][i-1]+result["width"][i-1]+result["height"][i-1]<result["left"][i]) or result["top"][i-1]+result["height"][i-1]*2 < result["top"][i])):
            finalresult = " ".join(array)
            array.clear()
            
            finalresult = translate.GetTranslate(finalresult, 'en', 'ko')
            overlay_screen_1.labeler(finalresult, minimum_left+arr[0]+8, minimum_top+arr[1]+30, result["left"][i]-minimum_left+result["width"][i], result["top"][i]-minimum_top+result["height"][i], result["height"][i])
            
            print(finalresult)
            print(result["left"][i]-minimum_left+result["width"][i])
            print(result["top"][i]-minimum_top+result["height"][i])
            print("----")
            minimum_left=10000
            minimum_top=10000
        elif(conf>70):#need to add 
            #tmptext = "".join([c if ord(c)<128 else "" for c in text]).strip()
            minimum_left = result["left"][i] if minimum_left > result["left"][i] else minimum_left
            minimum_top = result["top"][i] if minimum_top > result["top"][i] else minimum_top
            array.append(result["text"][i])
            print(minimum_left)
            print(minimum_top)
            
            
    frame1.after(1000,while_loop)

#--------------------------------------------------------------------



#--------------------------------------------------------------------

frame1 = tkinter.Tk()
frame1.title("Bridge - OCR Translator")
frame1.geometry("640x400+100+100")
#frame2 = tkinter.Tk()
overlay_screen_1 = Overlay(frame1)

#--------------------------------------------------------------------

#button1 = tkinter.Button(frame1, text = 'Start OCR', background='white')
#button1.pack()
#button1.config(command=button1_pressed)
frame1.after(1000,while_loop)
frame1.mainloop()

