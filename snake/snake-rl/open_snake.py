import sys
import os
import win32gui
import win32api
import win32con
import win32api
import subprocess
import time
import pyautogui


def run_snake():
    snake_exec_path = "../../Game/Snake.exe"
    app_instance = subprocess.Popen(snake_exec_path)
    hwndMain = win32gui.FindWindow(None,"Snake")
    return app_instance, hwndMain

def do_left(process,handle):    #not working yet
    #hwndCurrent = win32gui.GetActiveWindow()
    #result = win32gui.SetActiveWindow(handle)
    pyautogui.press('left')

    #win32gui.SetActiveWindow(hwndCurrent)
