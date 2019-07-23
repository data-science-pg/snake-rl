import cv2
import numpy as np
from PIL import ImageGrab
from open_snake import *

class CVDetector:

    def main_loop(self, app_handle: AppHandler):
        if(app_handle == 0):
            raise Exception("wrong handler format")
        __main_window = cv2.namedWindow("Snake Window")
        while(True):
            __printscreen_pil = ImageGrab.grab()
            __printscreen_numpy = np.array(__printscreen_pil.getdata(),dtype='uint8').reshape((__printscreen_pil.size[1],__printscreen_pil.size[0],3)) 
            cv2.imshow("Snake Window",__printscreen_numpy)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
        
    def __init__(self):
        pass