import cv2
import numpy as np

class CVDetector:
    m_mat = np.zeros((256, 256, 1), dtype = "uint8")

    def __init__(self):
        print("Ctor")