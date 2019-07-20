from CV_Detection import *
from open_snake import *
import time

def main():

    try:
        handler = AppHandler()
        #ImageDetection = CVDetector()

        handler.open()
        time.sleep(5)
        handler.do_left()
        print(handler.get_hwnd_main())
        time.sleep(3)
    except():
        print("Error")
    finally:
        handler.close()


main()
