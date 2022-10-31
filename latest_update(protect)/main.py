from fnmatch import translate
import cv2 as cv
import numpy as np
import os
import pytesseract
import matplotlib.pyplot as plt
import time, tkinter
import translate

from overlay import Overlay
from asyncio.windows_events import NULL
from hashlib import new
from capture_window import Capture_Window
from tesseract_ocr import Tesseract_Ocr
from pytesseract import Output

#----------------------initialize-----------------------------------
os.chdir(os.path.dirname(os.path.abspath(__file__)))

trocr = Tesseract_Ocr()
loop_time = time.time()


# return list of window name
# next patch : + gui select screen

Capture_Window.list_window_names()
window_name = input()

if(window_name == 'Desktop'):
    caps = Capture_Window()
else:
    caps = Capture_Window(window_name)
    
#--------------------------------------------------------------------


#--------------------------------------------------------------------
def button1_pressed():
    global overlay_screen
    
    if 'overlay_screen' in globals():
        overlay_screen.stop()
        del overlay_screen
    else:
        overlay_screen = Overlay(frame1)
        translated_overlay_on()
#--------------------------------------------------------------------


#--------------------------------------------------------------------
def translated_overlay_on():
    for i in range(0, len(result_text["text"])):
        
        conf = int(result_text["conf"][i])
        
        if conf > 70:
            text = result_text["text"][i]
            #text = translate.GetTranslate(text, 'en','ko')
            
            text = "".join([c if ord(c)<128 else "" for c in text]).strip()
            #cv2.rectangle(rgb_image, (x,y), (x + w, y + h), (0,255, 0), 2)
            #cv2.putText(rgb_image, text,(x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,200),2)
            overlay_screen.labeler(text, result_text["left"][i], result_text["top"][i], result_text["width"][i], result_text["height"][i])
            
            
    #rgb_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)
    #cv.imshow('Computer Vision', result_image)
    
#--------------------------------------------------------------------   


    
while(True):
    #statuswindow = caps.get_screen_minimize()
    #if(statuswindow == 1):
    screenshot = caps.get_screenshot()
    result_text = trocr.Get_Ocr_Tesseract(screenshot)

    frame1 = tkinter.Tk()
    button1 = tkinter.Button(frame1, text = 'Overlay', background='white')
    button1.pack()
    button1.config(command=button1_pressed)
    frame1.mainloop()
        

    
        
    #print('FPS {}', format(1/(time.time()-loop_time)))
    #loop_time = time.time()
    


"""
if cv.waitKey(1)==ord('q'):
    cv.destroyAllWindows()
    break
"""


    