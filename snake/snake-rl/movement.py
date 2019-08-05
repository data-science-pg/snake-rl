import pyautogui
from win32 import win32gui
from open_snake import AppHandler
import pywinauto

class Movement:

   
    @staticmethod
    def move_left(handler):    #not working yet
        #hwndCurrent = win32gui.GetActiveWindow()
        #result = win32gui.SetActiveWindow(handle)
        handler.SetOnTop()
        pywinauto.keyboard.send_keys("{LEFT}")
        #pyautogui.press('left')

    @staticmethod
    def move_right(handler):
        handler.SetOnTop()
        pywinauto.keyboard.send_keys("{RIGHT}")

    @staticmethod
    def move_down(handler):
        handler.SetOnTop()
        pywinauto.keyboard.send_keys("{DOWN}")

    @staticmethod
    def move_up(handler):
        handler.SetOnTop()
        pywinauto.keyboard.send_keys("{UP}")



