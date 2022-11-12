from ast import Not
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
win = tkinter.Tk()
win.title("Bridge")
win.geometry("640x480+100+100")
listbox = tkinter.Listbox(win, height=0)

os.chdir(os.path.dirname(os.path.abspath(__file__)))

Capture.list_window_names(listbox)
looptime = time.time()

#------------------------------variable------------------------------
global overlay_screen_1
global overlay_screen_2
global overlay_switch
global caps
global ocrs
overlay_switch = True

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

def while_loop(seleted_str):
    string = ""
    for i in listbox.curselection():
        string += str(listbox.get(i))

    if(string == "" ):
        frame1.after(100,while_loop,"")
        return

    global caps
    global ocrs
    if not (string == seleted_str):
        caps = Capture(string)
        ocrs = Tesseract_Ocr()
    global overlay_screen_2
    global overlay_screen_1
    global overlay_switch
    
    arr=caps.get_rect()#arr[0] = x, arr[1]=y
    screenshot = caps.get_screenshot()
    if(overlay_switch == False):
        overlay_screen_1 = Overlay(frame1)
    else:
        overlay_screen_2 = Overlay(frame2)
    result,str_result = ocrs.Get_Ocr_Tesseract(screenshot)
    #str_result(translate.GetTranslate(str_result, 'ko', 'en'))
    for i in range(0, len(result["text"])):

        text = result["text"][i]
        conf = int(result["conf"][i])
        
        if(conf>80):
            tmptext = "".join([c if ord(c)<128 else "" for c in text]).strip()
            if(tmptext != ""):
                #tmptext = translate.GetTranslate(tmptext, 'en', 'ko') 번역
                if(overlay_switch == False):
                    overlay_screen_1.labeler(tmptext,result["left"][i]+arr[0]+8,result["top"][i]+arr[1]+30)
                else:
                    overlay_screen_2.labeler(tmptext,result["left"][i]+arr[0]+8,result["top"][i]+arr[1]+30)
            #overlay_screen_2.labeler(tmptext,result["left"][i],result["top"][i])
            
    


    if(overlay_switch == True):
        overlay_screen_1.win.destroy()
        print("--- overlay_1 Delete Done ---")
    else:
        overlay_screen_2.win.destroy()
        print("--- overlay_2 Delete Done ---")
    overlay_switch = not overlay_switch
    frame1.after(1000,while_loop,string)


#--------------------------------------------------------------------



#--------------------------------------------------------------------


listbox.pack()
frame1 = tkinter.Frame(win)
frame2 = tkinter.Frame(win)

#frame2 = tkinter.Tk()
overlay_screen_1 = Overlay(frame1)
overlay_screen_2 = Overlay(frame2)



#--------------------------------------------------------------------
#global overlay_screen_2
#overlay_screen_2 = Overlay(frame2)
#global overlay_switch
#overlay_switch = False
#button1 = tkinter.Button(frame1, text = 'Start OCR', background='white')
#button1.pack()
#button1.config(command=button1_pressed)
frame1.after(1000,while_loop,"")
frame1.mainloop()
frame2.mainloop()
overlay_screen_1.win.mainloop()
overlay_screen_2.win.mainloop()



    