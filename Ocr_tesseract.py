import numpy as np
import cv2, pytesseract
import win32gui, win32ui, win32con
import Translate, Overlay
import Overlay,time,Quick,tkinter

from pyparsing import nullDebugAction
from pytesseract import Output
from asyncio.windows_events import NULL
from hashlib import new

w = 1920
h = 1080
bmpfilenamename = "Out.bmp"
windowname = "vscode"

hwnd = win32gui.FindWindow(None, windowname)
wDC = win32gui.GetWindowDC(hwnd)
dcObj=win32ui.CreateDCFromHandle(wDC)
cDC=dcObj.CreateCompatibleDC()
dataBitMap = win32ui.CreateBitmap()
dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
cDC.SelectObject(dataBitMap)
cDC.BitBlt((0,0),(w, h) , dcObj, (0,0), win32con.SRCCOPY)
dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)

screenshot = cv2.imread("Out.bmp")
screenshot = np.array(screenshot)
screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

texts = pytesseract.image_to_string(screenshot, lang='kor+eng')
result = pytesseract.image_to_data(screenshot, lang='kor+eng', output_type=Output.DICT) #테서렉트에서 좌표값 뽑아옴.

print(texts)
print("------------------")
print(result)
print("------------------")

main = tkinter.Tk()
a=Overlay.Overlay(main)

for i in range(1, len(result["text"])):
    x = result["left"][i]
    y = result["top"][i]
    tempy = result["top"][i-1]

    w = result["width"][i]
    h = result["height"][i]
    text = result["text"][i]
    conf = int(result["conf"][i])
    
    tmptext = "".join([c if ord(c)<128 else "" for c in text]).strip()
    print(tmptext)
    # while y++, until another cracter is come
    if(conf>70):
        a.labeler(tmptext,x,y, (int)(w/2))
        tmptext = NULL
        #tmptext = Translate.Trans(tmptext, eng, kor)
        
    
    """
    if conf > 70:
        text = "".join([c if ord(c)<128 else "" for c in text]).strip()
        #cv2.rectangle(rgb_image, (x,y), (x + w, y + h), (0,255, 0), 2)
        #cv2.putText(rgb_image, text,(x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,200),2)
        a = Overlay.Overlay(main)
        
        
        
        a.labeler("TEST",x,y)
    """

# Free Resources
dcObj.DeleteDC()
cDC.DeleteDC()
win32gui.ReleaseDC(hwnd, wDC)
win32gui.DeleteObject(dataBitMap.GetHandle())

button = tkinter.Button(main,text = 'Overlay',background='white')
button.pack()
main.mainloop()