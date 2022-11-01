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

from PIL import ImageGrab
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
    
    #global overlay_screen_2
    global overlay_screen_1
    #global overlay_switch
    overlay_screen_1 = Overlay(frame1)
    #overlay_screen_2 = Overlay(frame2)
    screenshot = caps.get_screenshot()
    result, str_result = ocrs.Get_Ocr_Tesseract(screenshot)
    for i in range(1, len(result["text"])):
        text = result["text"][i]
        conf = int(result["conf"][i])
    
        # while y++, until another cracter is come
        
        if(conf>70):
            tmptext = "".join([c if ord(c)<128 else "" for c in text]).strip()
            print(str_result)
            tmptext = translate.GetTranslate(tmptext, 'ko', 'en')
            arr=caps.get_rect()#arr[0] = x, arr[1]=y
            overlay_screen_1.labeler(tmptext,result["left"][i]+arr[0]+8,result["top"][i]+arr[1]+30, result["width"][i], result["height"][i])
            #overlay_screen_2.labeler(tmptext,result["left"][i],result["top"][i])
            
            #tmptext = NULL
            #tmptext = Translate.Trans(tmptext, eng, kor)
    print(str_result)
    print(translate.GetTranslate(str_result, 'ko', 'en'))
    """
    if(overlay_switch == True):
        overlay_screen_1.stop()
        print("overlay_1")
    else:
        overlay_screen_2.stop()
        print("overlay_2")
    overlay_switch = not overlay_switch
    """
    #overlay_screen_1.win.destroy()
    frame1.after(1000,while_loop)
    


#--------------------------------------------------------------------



#--------------------------------------------------------------------

frame1 = tkinter.Tk()
frame1.title("Bridge - OCR Translator")
frame1.geometry("640x400+100+100")
#frame2 = tkinter.Tk()
global overlay_screen_1
overlay_screen_1 = Overlay(frame1)

#--------------------------------------------------------------------
#global overlay_screen_2
#overlay_screen_2 = Overlay(frame2)
#global overlay_switch
#overlay_switch = False
#button1 = tkinter.Button(frame1, text = 'Start OCR', background='white')
#button1.pack()
#button1.config(command=button1_pressed)
frame1.after(1000,while_loop)
frame1.mainloop()

