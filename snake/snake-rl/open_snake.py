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
    
    def move_left(self):    #not working yet
        #hwndCurrent = win32gui.GetActiveWindow()
        #result = win32gui.SetActiveWindow(handle)
        pyautogui.press('left')
    
        #win32gui.SetActiveWindow(hwndCurrent)
    
    def close(self):
       # if self.app_instance!=None:
       if type(self.__app_instance) == subprocess.Popen:
            self.__app_instance.terminate()

    def Xpos(self):
        if(self.__hwnd_main == 0):
            return 0
        self.__x_pos  =  win32gui.GetWindowRect(self.__hwnd_main)[0]
        return self.__x_pos

    def Ypos(self):
        if(self.__hwnd_main == 0):
            return 0
        self.__y_pos  =  win32gui.GetWindowRect(self.__hwnd_main)[1]
        return self.__y_pos

    def Width(self):
        if(self.__hwnd_main == 0):
            return 0
        self.__width  =  win32gui.GetWindowRect(self.__hwnd_main)[2] - self.Xpos()
        return self.__width

    def Height(self):
        if(self.__hwnd_main == 0):
            return 0
        self.__heigth  =  win32gui.GetWindowRect(self.__hwnd_main)[2] - self.Ypos()
        return self.__heigth

        