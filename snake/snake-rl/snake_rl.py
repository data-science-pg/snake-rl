from CV_Detection import *
from open_snake import *
import time

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

        ImageDetection.main_loop(handler)
        handler.move_left()
        time.sleep(3)
    except():
        print("Error")
    finally:
        handler.close()


main()
