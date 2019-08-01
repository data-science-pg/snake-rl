import cv2
import numpy as np
from PIL import ImageGrab
from open_snake import *

class CVDetector:

    def main_loop(self, app_handle: AppHandler):
        if(app_handle == 0):
            raise Exception("wrong handler format")
        __main_window = cv2.namedWindow("Snake Window")

        while(app_handle.IsOpen()):
            rect = app_handle.Rect()
            if rect is None:
                break

            __printscreen_pil = ImageGrab.grab(rect)
            __printscreen_numpy = np.array(__printscreen_pil.getdata(),dtype='uint8').reshape((__printscreen_pil.size[1],__printscreen_pil.size[0],3))
            
            width = app_handle.Width()
            height = app_handle.Height()

            if height is None or width is None:
                break

            __printscreen_numpy = cv2.resize(__printscreen_numpy,(int(width/2),int(height/2)))

            CVDetector.swap_channels(__printscreen_numpy,0,2)
 
            
            cv2.imshow("Snake Window",__printscreen_numpy)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

    @staticmethod
    def swap_channels(img,first_idx,second_idx):
        channel = img[:,:,first_idx].copy()
        img[:,:,first_idx] = img[:,:,second_idx]
        img[:,:,second_idx] = channel

    def __init__(self):
        pass