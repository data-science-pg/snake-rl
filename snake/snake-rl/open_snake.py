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
from pywinauto import application
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
        if(False==self.IsOpen()):
            return None
        return win32gui.GetWindowRect(self.__hwnd_main)[0]

    def Ypos(self):
        if(False==self.IsOpen()):
            return None
        return  win32gui.GetWindowRect(self.__hwnd_main)[1]

    def Width(self):
        if(False==self.IsOpen()):
            return None
        return win32gui.GetWindowRect(self.__hwnd_main)[2] - self.Xpos()

    def Height(self):
        if(False==self.IsOpen()):
            return None
        return win32gui.GetWindowRect(self.__hwnd_main)[3] - self.Ypos()

    def Rect(self):
        if(False==self.IsOpen()):
            return None
        return win32gui.GetWindowRect(self.__hwnd_main)

    def IsOpen(self):
        if(self.__hwnd_main == 0 or False == win32gui.IsWindow(self.__hwnd_main)):
            return False    
        else:
            return True

    def SetOnTop(self):
        if(self.IsOpen() == True):
            app = application.Application()
            app.connect(handle = self.__hwnd_main)
            appDialog = app.window(title_re= "Snake")
            if(appDialog.exists()):
                appDialog.set_focus()
            else:
                return None
        else:
            return "Snake application is closed."
            
        