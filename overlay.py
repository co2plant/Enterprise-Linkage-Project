import tkinter, win32api, win32con, pywintypes
from win32api import GetSystemMetrics

class Overlay():
    
    def __init__(self,window):
        self.win = tkinter.Toplevel(window) #윈도우 객체 생성
        self.win.config(bg = '#add123') #윈도우 백그라운드 컬러 설정
        self.win.wm_attributes('-transparentcolor','#add123') # 설정한 컬러 투명화
        self.win.attributes("-fullscreen", True) # 전체화면
        self.win.wm_attributes("-topmost", True) # 윈도우가 항상 우선순위됨
        self.win.wm_attributes("-disabled", True) # 윈도우가 사리지지않음
        self.win.overrideredirect(True) # 작업표시줄 삭제

    def labeler(self,text_, x_, y_): # 윈도우창,텍스트,좌표x,좌표y
        label=tkinter.Label(self.win, text=text_, font=('Times','10'), fg="white", bg="black") #라벨 객체 생성 , bg='black'
        label.place(x=x_,y=y_) # 라벨 위치 설정
        #label.config(width = width_)
        #label.config(height = height_)
        #label.master.wm_attributes("-alpha", "0.5")
        label.master.lift()
        hWindow = pywintypes.HANDLE(int(label.master.frame(), 16)) # 클릭 무시
        exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT # 클릭무시 222
        win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle) #클릭 무시 3333

    def stop(self):
        self.win.destroy()
    def start(self):
        self.win.mainloop()