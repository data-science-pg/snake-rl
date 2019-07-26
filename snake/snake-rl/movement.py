import pyautogui

class Movement:
    def move_left(self):    #not working yet
        #hwndCurrent = win32gui.GetActiveWindow()
        #result = win32gui.SetActiveWindow(handle)
        pyautogui.press('left')
    
        #win32gui.SetActiveWindow(hwndCurrent)
    def move_right(self):
        pyautogui.press("right")

    def move_down(self):
        pyautogui.press("down")

    def move_up(self):
        pyautogui.press("up")



