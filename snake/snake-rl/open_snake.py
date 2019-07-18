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
        self.hwnd_main = win32gui.FindWindow(None,"Snake")
    
    def do_left(self):    #not working yet
        #hwndCurrent = win32gui.GetActiveWindow()
        #result = win32gui.SetActiveWindow(handle)
        pyautogui.press('left')
    
        #win32gui.SetActiveWindow(hwndCurrent)
    
    def close(self):
        if self.app_instance!=None:
            self.app_instance.terminate()

        