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
    hWndMain = None
    app_instance = None

    def __init__(self):
        self.snake_exec_path = "../../Game/Snake.exe"

    def Open(self):
        self.app_instance = subprocess.Poterminatepen(snake_exec_path)
        self.hwndMain = win32gui.FindWindow(None,"Snake")
    
    def do_left(self):    #not working yet
        #hwndCurrent = win32gui.GetActiveWindow()
        #result = win32gui.SetActiveWindow(handle)
        pyautogui.press('left')
    
        #win32gui.SetActiveWindow(hwndCurrent)
    
    def Close(self):
        time.sleep(5)
        self.do_left()
        time.sleep(1)
        self.app_instance.kill()

        