import numpy as np
import win32gui, win32ui, win32con

class Capture:
    
    width = 0
    height = 0
    hwnd = None
    cropped_x = 0
    cropped_y = 0
    offset_x = 0
    offset_y = 0
    
    def __init__(self, window_name=None):
        if window_name is None:
            self.hwnd = win32gui.GetDesktopWindow()
        else :
            self.hwnd = win32gui.FindWindow(None, window_name)
            print(self.hwnd)
            if not self.hwnd:
                raise Exception('Window not found: {}'.format(window_name))
        global left, top, right, bottom
        left, top, right, bottom = win32gui.GetWindowRect(self.hwnd)
        self.width = right-left
        self.height = bottom-top
        
        border_pixels = 8
        titlebar_pixels= 30
        self.width = self.width - (border_pixels * 2)
        self.height = self.height - titlebar_pixels - border_pixels
        self.cropped_x = border_pixels
        self.cropped_y = titlebar_pixels
        
        # need to change for caputure title
        # even if user don't want translate window title
        # disable this function.
        
        self.offset_x = left + self.cropped_x
        self.offset_y = top + self.cropped_y
        
    def get_screenshot(self):
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.width, self.height)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (self.width, self.height), dcObj, (self.cropped_x, self.cropped_y), win32con.SRCCOPY)
        
        
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.height, self.width, 4)
        
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())
        
        img = img[...,:3]
        
        img = np.ascontiguousarray(img)
        return img
    
    
    @staticmethod
    def list_window_names(listbox):
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                str = win32gui.GetWindowText(hwnd)
                if not(str == ""):
                    listbox.insert(-1, str)
        win32gui.EnumWindows(winEnumHandler, None)
        
    def get_screen_position(self, pos):
        print(pos[0]+self.offset_x)
        print(pos[1]+self.offset_y)
        return(pos[0]+self.offset_x, pos[1]+self.offset_y)
    
    def get_screen_minimize(self):
        statusofwindow = win32gui.GetWindowPlacement(self.hwnd)
        if statusofwindow[1] == win32con.SW_SHOWMINIMIZED:
            return 0
        elif statusofwindow[1] == win32con.SW_SHOWNORMAL:
            return 1
        
    def get_rect(self):
        left, top, right, bottom = win32gui.GetWindowRect(self.hwnd)
        return left, top