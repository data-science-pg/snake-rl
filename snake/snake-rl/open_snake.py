import sys
import os
import win32gui
import win32api
import win32con
import win32api
import subprocess
import time
import pyautogui

class AppHandler:
    
    snake_exec_path = None
    hwnd_main = None
    app_instance = None

    def __init__(self):
        self.snake_exec_path = "../../Game/Snake.exe"

    def open(self):
        self.app_instance = subprocess.Popen(self.snake_exec_path)
    
    def get_hwnd_main(self):
        if self.hwnd_main==None:
            self.hwnd_main = win32gui.FindWindow(None,"Snake")
        return self.hwnd_main;

    def do_left(self):    #not working yet
        #hwndCurrent = win32gui.GetActiveWindow()
        #result = win32gui.SetActiveWindow(handle)
        pyautogui.press('left')
    
        #win32gui.SetActiveWindow(hwndCurrent)

    def get_rect(self):
            rect = win32gui.GetWindowRect(self.get_hwnd_main())
            x = rect[0]
            y = rect[1]
            w = rect[2] - x
            h = rect[3] - y
            #WIP
    
    def close(self):
        if self.app_instance!=None:
            self.app_instance.terminate()

        