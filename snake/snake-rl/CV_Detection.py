import cv2
import numpy as np
from PIL import ImageGrab
from open_snake import *

class CVDetector:

    def main_loop(self, app_handle: AppHandler):
        if(app_handle == 0):
            raise Exception("wrong handler format")

        __window_name = "Snake Window"
        __main_window = cv2.namedWindow(__window_name)

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

            __printscreen_numpy = self.preprocess_image(__printscreen_numpy,width,height)
            
            #todo: rozmiar filtra powoduje exception
            #https://docs.opencv.org/3.1.0/d4/d13/tutorial_py_filtering.html
            
            cv2.imshow(__window_name,__printscreen_numpy)
            if (cv2.waitKey(25) and 0xFF == ord('q')):
                x = cv2.getWindowImageRect(__window_name)
                cv2.destroyAllWindows()
                break

    @staticmethod
    def swap_channels(img: np.ndarray,first_idx: int,second_idx: int):
        channel = img[:,:,first_idx].copy()
        img[:,:,first_idx] = img[:,:,second_idx]
        img[:,:,second_idx] = channel

    def preprocess_image(self,image: np.ndarray,width: int,height: int):
        image = cv2.resize(image,(int(width/2),int(height/2)))
        CVDetector.swap_channels(image,0,2)
        image = cv2.medianBlur(image,5)
        ret,image = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
        image = cv2.Canny(image,100,200)
        return image

    def __init__(self):
        pass