import clipboard,tkinter,time

class Quick():
    def __init__(self,win):
        self.window = tkinter.Toplevel(win)
        self.window.overrideredirect(True)
        self.text_var = tkinter.StringVar()
        self.window.bind("<KeyPress>",self.keyPressHandler)
        self.entry = tkinter.Entry(self.window,textvariable=self.text_var)
        self.entry.pack()
        self.entry.focus_set()
        self.window.after(100,self.loop)
    def loop(self):
        clipboard.copy(self.text_var.get())
        self.window.after(100,self.loop)

    def keyPressHandler(self,event):
        if event.keycode == 113:
            self.window.destroy()

    def start(self):
        self.window.mainloop()

    def stop(self):
        self.window.destroy()