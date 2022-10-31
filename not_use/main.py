import cv2 as cv
from capture_window import Capture_window
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

#--------------------------------------------------------------------

os.chdir(os.path.dirname(os.path.abspath(__file__)))

Capture_window.list_window_names()
window_name=input()

caps = Capture_window(window_name)

looptime = time.time()


#--------------------------------------------------------------------
#--------------------------------------------------------------------

def button1_pressed():
    global overlay_screen
    
    if 'overlay_screen' in globals():
        overlay_screen.stop()
        del overlay_screen
    else:
        overlay_screen = Overlay(frame1)

#--------------------------------------------------------------------
#--------------------------------------------------------------------

def while_loop():
    screenshot = caps.get_screenshot()
    screenshot.save("screenshot.png")
    frame1.after(1000,while_loop())

#--------------------------------------------------------------------




frame1 = tkinter.Tk()
button1 = tkinter.Button(frame1, text = 'Start OCR', background='white')
button1.pack()
button1.config(command=button1_pressed)
frame1.after(1000,while_loop())
frame1.mainloop()

    