import cv2 
import time 
import numpy as np

def Get_Image_Parameter(img_path):
    img = cv2.imread(img_path)
    print(img.shape)
    

if __name__ == "__main__":
    file_dir = "./"
    file_name = "00001.jpg"
    file_path = file_dir + file_name
    Get_Image_Parameter(file_path)
