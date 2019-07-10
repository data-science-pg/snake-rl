import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import subprocess
import win32gui
import win32con
import win32api
import time

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Snake Reinforcement learning GUI'
        self.snake_exec_path = "../../Game/Snake.exe"
        self.width = 320
        self.height = 200
        self.left = (1920 - self.width)/2.0
        self.top = (1080 - self.height)/2.0
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        run_button = QPushButton('Run Snake', self)
        self.set_position(run_button,self.width/2.0,self.height/2.0)
        run_button.clicked.connect(self.on_click_run)

        press_left_button = QPushButton("Test Input",self)
        self.set_position(press_left_button,run_button.x()+run_button.width()/2.0,run_button.y()+run_button.height()+10);
        press_left_button.clicked.connect(self.on_click_left)
        
        self.show()

    @pyqtSlot()
    def on_click_run(self):
        self.app_instance = subprocess.Popen(self.snake_exec_path)
        self.hwndMain = win32gui.FindWindow(None,"Snake")

    @pyqtSlot()
    def on_click_left(self):    #not working yet
        hwndCurrent = win32gui.GetActiveWindow();
        win32gui.SetActiveWindow(self.hwndMain);
        #virtual_key = win32api.MapVirtualKey(win32con.VK_LEFT, 0);
        result = win32api.PostMessage(self.hwndMain, win32con.WM_KEYDOWN, win32con.VK_LEFT, 21692417);#magic value extracted from debug
        print(result)
        time.sleep(0.2)
        win32api.PostMessage(self.hwndMain, win32con.WM_KEYUP, win32con.VK_LEFT, -1052049407);#magic value extracted from debug
        #todo: check how to add keyboard input

    def set_position(self,widget,x,y):
        widget.move(x-widget.width()/2.0,y-widget.height()/2.0)

def run_open_snake():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())