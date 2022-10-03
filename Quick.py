import clipboard,tkinter,time
from Translate import Trans

class Quick():
    def __init__(self,win):
        self.window = tkinter.Toplevel(win) #윈도우 최상단 위치
        self.window.overrideredirect(True) #상태표시줄 삭제
        self.text_var = tkinter.StringVar() # 스트링
        self.window.bind("<KeyPress>",self.keyPressHandler) #키입력 이벤트 할당
        self.entry = tkinter.Entry(self.window,textvariable=self.text_var) #입력창
        self.entry.pack()
        self.entry.focus_set() #입력창에 기본 버퍼

    def keyPressHandler(self,event):
        if event.keycode == 113: #f2
            str = self.text_var.get()
            clipboard.copy(Trans(str,"ko","en")) #클립보드에 입력창 문구를 ko에서 en으로 번역 후 저장
            self.window.destroy()

    def start(self):
        self.window.mainloop()

    def stop(self):
        self.window.destroy()