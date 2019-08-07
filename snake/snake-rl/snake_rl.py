from CV_Detection import *
from open_snake import *
import time
from movement import *
from threading import Thread
import subprocess

def main():

    try:
        handler = AppHandler()
        ImageDetection = CVDetector()

        handler.open()

        #Getters test
        print(handler.Xpos())
        print(handler.Ypos())
        print(handler.Width())
        print(handler.Height())

        time.sleep(3)
        
        Movement.move_left(handler)
        p1=Thread(target=ImageDetection.main_loop(handler))

        p1.start()


        Movement.move_left(handler)
        time.sleep(2)
        Movement.move_left(handler)
        time.sleep(2)
        Movement.move_left(handler)
        time.sleep(2)
        Movement.move_left(handler)
        time.sleep(2)
    except():
        print("Error")
    finally:
        handler.close()


main()
