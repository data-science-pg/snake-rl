import pyautogui

class Movement:

    @staticmethod
    def move_left():    #not working yet
        #hwndCurrent = win32gui.GetActiveWindow()
        #result = win32gui.SetActiveWindow(handle)
        pyautogui.press('left')
    
        #win32gui.SetActiveWindow(hwndCurrent)

    @staticmethod
    def move_right():
        pyautogui.press("right")

    @staticmethod
    def move_down():
        pyautogui.press("down")

    @staticmethod
    def move_up():
        pyautogui.press("up")



