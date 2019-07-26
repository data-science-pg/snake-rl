import sys
import os
#import win32gui
#import win32api
#import win32con
#import win32api
from win32 import win32gui
import win32ui, win32con, win32api
import subprocess
import time
import pyautogui

class AppHandler:

    def __init__(self):
        self.__snake_exec_path = "../../Game/Snake.exe"

    def open(self):
        self.__app_instance = subprocess.Popen(self.__snake_exec_path)
        time.sleep(5)
        self.__hwnd_main = win32gui.FindWindow(None,"Snake")
        
    def close(self):
       # if self.app_instance!=None:
       if type(self.__app_instance) == subprocess.Popen:
            self.__app_instance.terminate()

    def Xpos(self):
        if(self.__hwnd_main == 0):
            return 0
        return win32gui.GetWindowRect(self.__hwnd_main)[0]

    def Ypos(self):
        if(self.__hwnd_main == 0):
            return 0
        return  win32gui.GetWindowRect(self.__hwnd_main)[1]

    def Width(self):
        if(self.__hwnd_main == 0):
            return 0
        return win32gui.GetWindowRect(self.__hwnd_main)[2] - self.Xpos()

    def Height(self):
        if(self.__hwnd_main == 0):
            return 0
        return win32gui.GetWindowRect(self.__hwnd_main)[3] - self.Ypos()

    def Rect(self):
        if(self.__hwnd_main == 0):
            return 0
        return win32gui.GetWindowRect(self.__hwnd_main)

    def IsOpen(self):
        if(self.__hwnd_main == 0 | win32gui.IsWindowEnabled(self.__hwnd_main)):
            return False    
        else:
            return True
        