from asyncio.windows_events import NULL
from hashlib import new
import Overlay,time,Quick,tkinter
def keyPressHandler(event):
        if event.keycode == 112:
            a = Overlay.Overlay(main)
            a.labeler("TEST",300,300)
        if event.keycode == 113:
            b = Quick.Quick(main)

def button_press():
    global a
    if 'a' in globals():
        a.stop()
        del a
    else:
        a = Overlay.Overlay(main)
        a.labeler("TEST",300,300)

main = tkinter.Tk()
button = tkinter.Button(main,text = 'Overlay',background='white')
button.pack()
button.config(command=button_press)
main.bind("<KeyPress>",keyPressHandler)
main.mainloop()
