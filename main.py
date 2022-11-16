

import os
import tkinter
from savecsv import SaveCsv
from asyncio.windows_events import NULL
from overlay import Overlay
from capture import Capture
from ocr import Tesseract_Ocr
import translate


Csv = SaveCsv() # class 선언부

def button_press():
    global B_dict
    count = 0
    if(len(S_dict) > 0):
        for i in range(0, len(S_dict)):
            if(Csv.serach(S_dict[i],'dictionary')== False and len(S_dict[i]) >= 1 and filtering_word(S_dict[i]) == False):
                Csv.saveDictionary(S_dict[i],translate.GetTranslate(S_dict[i], 'en', 'ko'),'dictionary')
                count += 1
#--------------------------------------------------------------------
win = tkinter.Tk() # TK 선언부
win.title("Bridge")
win.geometry("440x300+100+100")
win.resizable(False, False)
listbox = tkinter.Listbox(win, height=0)
listbox.place(x=10,y=10,width=418,height=250)
button = tkinter.Button(win,text = 'Make Dictionary' )
button.config(command=button_press)
button.place(x=328,y=267.5,width=100)

os.chdir(os.path.dirname(os.path.abspath(__file__)))
Capture.list_window_names(listbox)


#------------------------------variable------------------------------
global overlay_screen_1
global overlay_screen_2
global overlay_switch
global caps
global ocrs
global S_dict
S_dict = list()
overlay_switch = True
array = []
be_verb = ['am','be','are','is','was','were','was','i','you','we','he','she','it','we','they','will'] # Be 동사는 단어장에 안들어감
#--------------------------------------------------------------------


def while_loop(seleted_str):
    file_name = ""
    for i in listbox.curselection():
        file_name += str(listbox.get(i))

    if(file_name == "" ):
        frame1.after(100,while_loop,"")
        return

    global caps
    global ocrs
    if not (file_name == seleted_str):
        caps = Capture(file_name)
        ocrs = Tesseract_Ocr()
    global overlay_screen_2
    global overlay_screen_1
    global overlay_switch
    global S_dict
    S_dict.clear()
    arr=caps.get_rect()#arr[0] = x, arr[1]=y
    screenshot = caps.get_screenshot()
    minimum_left=10000
    minimum_top=10000
    if(overlay_switch == False):
        overlay_screen_1 = Overlay(frame1)
    else:
        overlay_screen_2 = Overlay(frame2)
    result,str_result = ocrs.Get_Ocr_Tesseract(screenshot)
    for i in range(0, len(result["text"])):
        
        text = result["text"][i]
        conf = int(result["conf"][i])
        
        if(((result["left"][i-1]+result["width"][i-1]+result["height"][i-1]<result["left"][i]) or result["top"][i-1]+result["height"][i-1]*1.2 < result["top"][i]) or i == len(result["text"])):
            finalresult = " ".join(array)
            array.clear()
            if(finalresult == NULL or len(finalresult) <= 1):
                continue

            search_text = Csv.serach(finalresult,file_name)

            if(search_text == False):
                temp_text = finalresult
                finalresult = translate.GetTranslate(finalresult, 'en', 'ko')
                Csv.saveDictionary(temp_text,finalresult,file_name)
                temp_text = NULL
            else:
                finalresult = search_text

            search_text = NULL
            if(len(finalresult) >= 1):
                if(overlay_switch == False):
                    overlay_screen_1.labeler(finalresult, minimum_left+arr[0]+8, minimum_top+arr[1]+30, result["left"][i]-minimum_left+result["width"][i], result["top"][i]-minimum_top+result["height"][i], 11)
                else:
                    overlay_screen_2.labeler(finalresult, minimum_left+arr[0]+8, minimum_top+arr[1]+30, result["left"][i]-minimum_left+result["width"][i], result["top"][i]-minimum_top+result["height"][i], 11)
            minimum_left=10000
            minimum_top=10000
        elif(conf>70):#need to add 
            tmptext = "".join([c if ord(c)<128 else "" for c in text]).strip()
            S_dict.append(tmptext)
            minimum_left = result["left"][i] if minimum_left > result["left"][i] else minimum_left
            minimum_top = result["top"][i] if minimum_top > result["top"][i] else minimum_top
            array.append(tmptext)


    if(overlay_switch == True):
        overlay_screen_1.win.destroy()
    else:
        overlay_screen_2.win.destroy()
    overlay_switch = not overlay_switch
    frame1.after(1000,while_loop,file_name)
#--------------------------------------------------------------------

def filtering_word(input_text):
    for i in range(0, len(be_verb)):
        if(input_text.lower() == be_verb[i]):
            return True
    return False

#--------------------------------------------------------------------

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

createFolder('./CSV')
 
#--------------------------------------------------------------------
frame1 = tkinter.Frame(win)
frame2 = tkinter.Frame(win)

overlay_screen_1 = Overlay(frame1)
overlay_screen_2 = Overlay(frame2)

frame1.after(1000,while_loop,"")
frame1.mainloop()
frame2.mainloop()
overlay_screen_1.win.mainloop()
overlay_screen_2.win.mainloop()



    