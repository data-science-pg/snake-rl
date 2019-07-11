import sys
import os
import win32gui
import win32con
import win32api
import subprocess
import time


def run_snake():
    snake_exec_path = "../../Game/Snake.exe"
    app_instance = subprocess.Popen(snake_exec_path)
    hwndMain = win32gui.FindWindow(None,"Snake")

def do_left():    #not working yet
    hwndMain = win32gui.FindWindow(None,"Snake")
    hwndCurrent = win32gui.GetActiveWindow()
    win32gui.SetActiveWindow(hwndMain)
    #virtual_key = win32api.MapVirtualKey(win32con.VK_LEFT, 0);
    result = win32api.PostMessage(hwndMain, win32con.WM_KEYDOWN, win32con.VK_LEFT, 21692417)#magic value extracted from debug
    print(result)
    time.sleep(0.2)
    win32api.PostMessage(hwndMain, win32con.WM_KEYUP, win32con.VK_LEFT, -1052049407)#magic value extracted from debug
    #todo: check how to add keyboard input