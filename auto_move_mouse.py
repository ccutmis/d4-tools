# PYAUTOGUI DOCUMENTATION : https://pyautogui.readthedocs.io/en/latest/
# INSTALL win32gui : pip install pywin32 或  pip install --upgrade pywin32==224
import win32gui
import pyautogui as pag
import re
import random
import time

# https://stackoverflow.com/questions/2090464/python-window-activation
class WindowMgr:
    """Encapsulates some calls to the winapi for window management"""

    def __init__ (self):
        """Constructor"""
        self._handle = None

    def find_window(self, class_name, window_name=None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """put the window in the foreground"""
        win32gui.SetForegroundWindow(self._handle)


def main():
    left,right,top,down=50,1000,50,1000
    w = WindowMgr()
    w.find_window_wildcard(".*Google*")
    w.set_foreground()
    while 1:
        w.set_foreground()
        x,y,dt= random.randint(left,right),random.randint(top,down),random.randint(1,4)
        pag.moveTo(x,y,dt)
        #pag.click() # 在當前滑鼠位置點一下
        #pag.press('1') # 按下 "1"
        print(x,y,dt)
        time.sleep(random.randint(1,4))

if __name__ == "__main__": main()