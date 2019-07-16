from CV_Detection import *
from open_snake import *
<<<<<<< HEAD

def main():

    run_snake()   #olek: run gui
    ImageDetection = CVDetector()
    print("Foo")
=======
import time

def main():

    process, handle = run_snake()   #olek: run gui
    time.sleep(5)
    do_left(process, handle)
    time.sleep(1)
    process.terminate()

    #ImageDetection = CVDetector()

>>>>>>> refs/remotes/origin/master
main()
