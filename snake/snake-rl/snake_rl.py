from CV_Detection import *
from open_snake import *
import time
from movement import *
from multiprocessing import Process

def main():

    try:
        handler = AppHandler()
        ImageDetection = CVDetector()
        movement = Movement()

        handler.open()

        #Getters test
        print(handler.Xpos())
        print(handler.Ypos())
        print(handler.Width())
        print(handler.Height())

        time.sleep(3)

        movement.move_left()
        p1=Process(target=ImageDetection.main_loop(handler))
        p1.start()

        movement.move_left()
        movement.move_right()
        movement.move_up()
        movement.move_down()
        time.sleep(3)
    except():
        print("Error")
    finally:
        handler.close()


main()
