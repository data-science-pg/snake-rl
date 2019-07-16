from CV_Detection import *
from open_snake import *
import time

def main():

    try:
        handler = AppHandler()
        ImageDetection = CVDetector()

        handler.Open()
    except():
        print("Error")
    finally:
        handler.Close()


main()
