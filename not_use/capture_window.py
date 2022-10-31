import numpy as np
import win32gui, win32ui, win32con
from time import time
from PIL import ImageGrab

class Capture_window:
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
        screenshot=ImageGrab.grab(bbox = (self.offset_x, self.offset_y, self.width, self.height))
        time.sleep(5)
        return screenshot

    @staticmethod
    def list_window_names():
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(winEnumHandler, None)

    def get_screen_position(self, pos):
        return(pos[0]+self.offset_x, pos[1]+self.offset_y)
    
    def get_screen_minimize(self):
        statusofwindow = win32gui.GetWindowPlacement(self.hwnd)
        if statusofwindow[1] == win32con.SW_SHOWMINIMIZED:
            return 0
        elif statusofwindow[1] == win32con.SW_SHOWNORMAL:
            return 1