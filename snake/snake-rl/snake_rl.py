from CV_Detection import *
from open_snake import *
import time
from movement import *

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

        time.sleep(10)
        Movement.move_left()
        Movement.move_right()
        Movement.move_up()
        Movement.move_down()

        time.sleep(3)
    except():
        print("Error")
    finally:
        handler.close()


main()
