import cv2
import numpy as np
from PIL import ImageGrab

class CVDetector:
    m_mat = np.zeros((256, 256, 1), dtype = "uint8")


    def main_loop():
        #while(True):
            printscreen_pil = ImageGrab.grab()
            printscreen_numpy = np.array(printscreen_pil.getdata(),dtype='uint8')\
            .reshape((printscreen_pil.size[1],printscreen_pil.size[0],3)) 
            cv2.imshow('window',printscreen_numpy)
            #if cv2.waitKey(25) & 0xFF == ord('q'):
            #    cv2.destroyAllWindows()
            #    break
        
    def __init__(self):
        print("Ctor")
        CVDetector.main_loop()