#########################################
# D4_WASD                 VERSION: 0.6A #
# UPDATE: 2023-05-20  AUTHOR: ALOHA3307 #
#########################################
PROJECT_NAME = 'D4_WASD V0.6A'

import keyboard
import threading
import time
from datetime import datetime
from sys import argv,exc_info,exit
from math import pi,sin,cos
from traceback import extract_tb

import win32gui, win32com.client, win32con, winxpgui, win32api, ctypes
from os import system
from time import sleep
from re import match
from subprocess import Popen,PIPE

MOUSE_LEFT_DOWN=0x0002
MOUSE_LEFT_UP=0x0004
MOUSE_RIGHT_DOWN=0x0008
MOUSE_RIGHT_UP=0x0010

class WindowMgr:
    def __init__ (self):
        self._handle = None
        self.is_exist = False
    def find_window(self, class_name, window_name=None):
        self._handle = win32gui.FindWindow(class_name, window_name)
    def _window_enum_callback(self, hwnd, wildcard):
        if match(".*?"+wildcard+"*", str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd
            self.is_exist = True
    def find_window_wildcard(self, wildcard):
        self._handle = None
        self.is_exist = False
        win32gui.EnumWindows(self._window_enum_callback, wildcard)
    def set_cmd_title(self,cmd_title):
        ctypes.windll.kernel32.SetConsoleTitleW(cmd_title)
        sleep(2)
    def active_window_title(self):
        return win32gui.GetWindowText(win32gui.GetForegroundWindow())
    def get_window_pos_size(self):
        try:
            rect = win32gui.GetWindowRect(win32gui.GetForegroundWindow())
        except:
            rect = win32gui.GetWindowRect(win32gui.GetDesktopWindow())
        x = rect[0]
        y = rect[1]
        w = rect[2] - x
        h = rect[3] - y
        return [x,y,w,h]
    def set_foreground(self):
        win32gui.SetForegroundWindow(self._handle)
    def set_window_state(self,tmp_window_state=''):
        if tmp_window_state=='MAX':
            win32gui.ShowWindow(self._handle, win32con.SW_SHOWMAXIMIZED)
        elif tmp_window_state=='MIN':
            win32gui.ShowWindow(self._handle, win32con.SW_SHOWMINIMIZED)
        else:
            win32gui.ShowWindow(self._handle, win32con.SW_SHOWNORMAL)
    def reset(self):
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
    def set_window_on_top(self, wildcard,win_w=320,win_h=240,set_top=True):
        self.reset()
        self.find_window_wildcard(wildcard)
        self.set_foreground()
        if set_top==True:
            win32gui.SetWindowPos(self._handle,win32con.HWND_TOPMOST,0,0,win_w,win_h,0)
        else:
            win32gui.SetWindowPos(self._handle,win32con.HWND_NOTOPMOST,0,0,win_w,win_h,0)
        sleep(0.5)
    def set_window_alpha(self, wildcard, alpha_val=180):
        self.reset()
        self.find_window_wildcard(wildcard)
        self.set_foreground()
        win32gui.SetWindowLong (self._handle, win32con.GWL_EXSTYLE, win32gui.GetWindowLong (self._handle, win32con.GWL_EXSTYLE ) | win32con.WS_EX_LAYERED )
        winxpgui.SetLayeredWindowAttributes(self._handle, win32api.RGB(0,0,0), alpha_val, win32con.LWA_ALPHA)


class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_ulong), ("y", ctypes.c_ulong)]

def get_pos():
    pt = POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
    return pt.x,pt.y

def move_to_abs(offx=0,offy=0):
    set_pos(offx,offy)
    return offx,offy

def set_pos(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)

def click(flag,x,y,updown=1):
    if flag=='left':
        if updown==1:
            ctypes.windll.user32.mouse_event(MOUSE_LEFT_DOWN, x, y, 0,0) # left down
        else:
            ctypes.windll.user32.mouse_event(MOUSE_LEFT_UP, x, y, 0,0) # left up
    elif flag=='right':
        if updown==1:
            ctypes.windll.user32.mouse_event(MOUSE_RIGHT_DOWN, x, y, 0,0) # left down
        else:
            ctypes.windll.user32.mouse_event(MOUSE_RIGHT_UP, x, y, 0,0) # left up

def gent_degree_dict(divisions=360,radius=1):
    out_dict={}
    angle = 2 * pi / divisions
    angles = [i*angle for i in range(divisions)]
    oi=0
    for a in angles:
        out_dict[oi]=[int(radius*sin(a)),(int(radius*cos(a)))]
        oi+=1
    return out_dict

def deg_to_xy(deg):
    global DEG_DICT
    xy_list=DEG_DICT[deg]
    return xy_list[0],-xy_list[1]

def detect_key_pressed():
    global KEY_LAST, KEY_CONFIG, RUN_PROGRAM,DELAY_SECOND,SYS_KEY_PRESSED,SYS_KEY_MAP,KEY_ONOFF,edit_flag,current,KEY_ALIAS,BTN_DICT
    KEY_LAST_CHECK = lambda x: True if keyboard.is_pressed(x) else False
    while RUN_PROGRAM:
        # 偵測鍵盤按鍵
        for i in KEY_ALIAS:
            num = BTN_DICT[i]
            KEY_LAST[num] = KEY_LAST_CHECK(KEY_CONFIG[i])
            if KEY_LAST[num]:
                if KEY_CONFIG[i] in KEY_ONOFF and edit_flag==True:
                    if KEY_CONFIG[i] not in current:
                        current.append(KEY_CONFIG[i])
                    else:
                        current.remove(KEY_CONFIG[i])
        SYS_KEY_PRESSED[0] = KEY_LAST_CHECK(SYS_KEY_MAP['SHOW_APP'])
        SYS_KEY_PRESSED[1] = KEY_LAST_CHECK(SYS_KEY_MAP['HIDE_APP'])
        SYS_KEY_PRESSED[2] = KEY_LAST_CHECK(SYS_KEY_MAP['EXIT_APP'])
        time.sleep(DELAY_SECOND) # 暫停 DELAY_SECOND 秒，避免繁忙的監控

if __name__ == '__main__':
    try:
        #讀入INI
        ini_filename="wasd_setting.txt"
        if len(argv)>1 and argv[1]!="" and (argv[1]).split(".")[1]=="txt":
            ini_filename=argv[1]
        #讀取 xinput.ini參數
        with open(ini_filename,"r",encoding="utf-8") as f:
            tmp_content=f.read()
        exec(tmp_content)
        # 宣告全域變數
        RUN_PROGRAM = True
        loop_flag=True
        edit_flag=False
        current = []
        CURSOR_XY_HISTORY =[ [0,0,0] ]

        # 建立執行緒
        all_key_thread = threading.Thread(target=detect_key_pressed, name='AllKeyThread')

        # 啟動執行緒
        all_key_thread.start()

        w=WindowMgr()
        w.set_cmd_title(f"{PROJECT_NAME}")
        w.reset()
        w.set_window_on_top(PROJECT_NAME,WINDOW_WH[0],WINDOW_WH[1])
        w.set_window_alpha(PROJECT_NAME, alpha_val=WINDOW_ALPHA)

        PRINT_VAR = lambda x: x if x!='' else 'NA'
        PRINT_TRUE_FALSE = lambda x: ' TRUE' if x==True else 'FALSE'
        PRINT_APP_ONOFF = lambda x: '啟用' if x==True else '暫停'
        DASH_LINE = "-"*50
        PRINT_CURRENT = lambda x: x[:10] if x!='set()' else 'NA'
        DEG_DICT = gent_degree_dict(radius=XY_OFFSET_UNIT)
        OX,OY = -1,-1
        CURSOR_OUT_RANGE = False
        ACTOR_MOVED = False
        PRIME_NUMBER = 53
        elapsed_time=0

        print(f"{PROJECT_NAME}  監控目標: {PRINT_VAR(ACTIVE_WIN_TITLE)}\n{DASH_LINE}\n快捷鍵: 上:{KEY_CONFIG['UP']} 下:{KEY_CONFIG['DOWN']} 左:{KEY_CONFIG['LEFT']} 右:{KEY_CONFIG['RIGHT']} LM:{PRINT_VAR(KEY_CONFIG['LM'])} RM:{PRINT_VAR(KEY_CONFIG['RM'])} 強制移動:{PRINT_VAR(KEY_CONFIG['FORCE_MOVE'])}")
        print(f"切換STATUS:{PRINT_VAR(KEY_CONFIG['APP_ON_OFF'])} 切換AAM:{PRINT_VAR(KEY_CONFIG['AAM_SWITCH'])} 切換游標復位:{PRINT_VAR(KEY_CONFIG['CURSOR_FLY_ON_OFF'])}")
        print(f"結束:Shift+Alt+X 顯示:Shift+Alt+S 隱藏:Shift+Alt+H")           
        print(f"{DASH_LINE}\nSTATUS\t| UNIT\t| 移動後(AAM)\t| 游標復位")

        while RUN_PROGRAM:
            elapsed_time+=1
            if SYS_KEY_PRESSED[0]:
                w.reset()
                w.find_window_wildcard(PROJECT_NAME)
                w.set_window_state()
            if SYS_KEY_PRESSED[1]:
                w.reset()
                w.find_window_wildcard(PROJECT_NAME)
                w.set_window_state('MIN')
            if KEY_LAST[12]:
                index = AAM_LIST.index(ACTION_AFTER_MOVE)
                max = len(AAM_LIST)
                index = index+1 if index+1 < max else 0
                ACTION_AFTER_MOVE = AAM_LIST[index]
                time.sleep(DELAY_SECOND)
            if KEY_LAST[13]:
                APP_ON_OFF = True if APP_ON_OFF==False else False
                time.sleep(DELAY_SECOND)
            if KEY_LAST[14]:
                CURSOR_FLY_AFTER_MOVE = True if CURSOR_FLY_AFTER_MOVE==False else False
                time.sleep(DELAY_SECOND)
            if SYS_KEY_PRESSED[2]:
                RUN_PROGRAM = False
            if keyboard.is_pressed("=") and keyboard.is_pressed("-") and keyboard.is_pressed("0"):
                keyboard.release(KEY_CONFIG['FORCE_MOVE'])
            print_str= f" {PRINT_APP_ONOFF(APP_ON_OFF)}\t| "+str(XY_OFFSET_UNIT).ljust(3," ")+f"\t| {AAM_DICT[PRINT_VAR(ACTION_AFTER_MOVE)]}\t|  {PRINT_TRUE_FALSE(CURSOR_FLY_AFTER_MOVE)}"

            print('\b'*len(print_str)+print_str,end='\r')

            if APP_ON_OFF and (ACTIVE_WIN_TITLE=="" or (ACTIVE_WIN_TITLE!="" and ACTIVE_WIN_TITLE in w.active_window_title())):
                # print(CURSOR_XY_HISTORY[-1])
                in_active_win=True
                win_pos_size=w.get_window_pos_size() #[x,y,w,h]
                x_center=int(win_pos_size[0]+(win_pos_size[2]/2))
                y_center=int(win_pos_size[1]+(win_pos_size[3]/2)+Y_CENTER_OFFSET)

                arrow_key_pressed_count = KEY_LAST[:4].count(True)
                CX,CY = get_pos()
                distance = ((CX - x_center) ** 2 + (CY - y_center) ** 2) ** 0.5
                if distance < XY_OFFSET_UNIT+10:
                    CURSOR_OUT_RANGE = False
                else:
                    CURSOR_OUT_RANGE = True
                    if CURSOR_XY_HISTORY[-1] != [1,CX,CY]:
                        CURSOR_XY_HISTORY.append([1,CX,CY])
                    OX,OY = CX,CY

                tx,ty,deg = 0,0,-1
                if arrow_key_pressed_count > 0 : #按下任意方向鍵
                    if arrow_key_pressed_count == 1:
                        if KEY_LAST[0]:
                            deg = COORDINATE[CURRENT_COORDINATE][0]
                        elif KEY_LAST[1]:
                            deg = COORDINATE[CURRENT_COORDINATE][4]
                        elif KEY_LAST[2]:
                            deg = COORDINATE[CURRENT_COORDINATE][6]
                        elif KEY_LAST[3]:
                            deg = COORDINATE[CURRENT_COORDINATE][2]
                    else:
                        if KEY_LAST[0] and KEY_LAST[3]:
                            deg = COORDINATE[CURRENT_COORDINATE][1]
                        elif KEY_LAST[1] and KEY_LAST[3]:
                            deg = COORDINATE[CURRENT_COORDINATE][3]
                        elif KEY_LAST[0] and KEY_LAST[2]:
                            deg = COORDINATE[CURRENT_COORDINATE][7]
                        elif KEY_LAST[1] and KEY_LAST[2]:
                            deg = COORDINATE[CURRENT_COORDINATE][5]
                    if deg!=-1:
                        ACTOR_MOVED = True
                        set_pos(x_center,y_center)
                        tx,ty=deg_to_xy(deg)
                        tx+=x_center
                        ty+=y_center
                        move_to_abs(int(tx),int(ty))
                        if ACTION_AFTER_MOVE == 'LM':
                            click('left',0,0,1)
                        elif ACTION_AFTER_MOVE == 'RM':
                            click('right',0,0,1)
                        elif ACTION_AFTER_MOVE == 'FORCE_MOVE':
                            keyboard.press(KEY_CONFIG['FORCE_MOVE'])
                        else: # ACTION_AFTER_MOVE ==""
                            pass
                        sleep(DELAY_SECOND)
                        # 判斷 mouse 位置是否同 tx,ty
                        if (tx,ty)!=get_pos():
                            if ACTION_AFTER_MOVE == 'LM':
                                click('left',0,0,0)
                            elif ACTION_AFTER_MOVE == 'RM':
                                click('right',0,0,0)
                            elif ACTION_AFTER_MOVE == 'FORCE_MOVE':
                                keyboard.release(KEY_CONFIG['FORCE_MOVE'])
                            else:
                                pass
                            sleep(DELAY_SECOND)
                else:
                    if ACTOR_MOVED:
                        if ACTION_AFTER_MOVE == 'LM':
                            click('left',0,0,0)
                        elif ACTION_AFTER_MOVE == 'RM':
                            click('right',0,0,0)
                        elif ACTION_AFTER_MOVE == 'FORCE_MOVE':
                            keyboard.release(KEY_CONFIG['FORCE_MOVE'])
                        else:
                            pass
                        if CURSOR_FLY_AFTER_MOVE:
                            set_pos(CURSOR_XY_HISTORY[-1][1],CURSOR_XY_HISTORY[-1][2])
                        ACTOR_MOVED = False
                if KEY_LAST[10]: # LM
                    click('left',0,0,1)
                    click('left',0,0,0)
                if KEY_LAST[11]: # RM
                    click('right',0,0,1)
                    click('right',0,0,0)
                if elapsed_time%int(DELAY_SECOND*PRIME_NUMBER)==0:
                    for i in current:
                        keyboard.press_and_release(i)
                edit_flag=True
            else:
                edit_flag=False
            time.sleep(DELAY_SECOND)

        # 等待執行緒結束
        all_key_thread.join()

        print("程式已經停止。")
    except Exception as e:
        error_class = e.__class__.__name__ #取得錯誤類型
        detail = e.args[0] #取得詳細內容
        cl, exc, tb = exc_info() #取得Call Stack
        lastCallStack = extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
        fileName = lastCallStack[0] #取得發生的檔案名稱
        lineNum = lastCallStack[1] #取得發生的行號
        funcName = lastCallStack[2] #取得發生的函數名稱
        errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
        with open('wasd_threading_runtime_error.log','a+',encoding='utf-8') as f:
            f.writelines(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\t'+errMsg+'\n')
        print(errMsg)
        exit(0)


