from DownloadImages import DownloadsImageFromWeb
from SplitImage import Split_Image
from SplitImage import Split_Captcha
import cv2 
import os
from color_anal import Compared_2img_With_hamming
def ImageRecognize(data_set_dir, img_path):
    # Log total count of number class 
    img_path_dict = {"0": [], "1": [], "2": [], "3": [],\
                     "4": [], "5": [], "6": [], "7": [],\
                     "8": [], "9":[] }
    per_img_hamming_distance= {"0": [], "1": [], "2": [], "3": [],\
                                "4": [], "5": [], "6": [], "7": [],\
                                "8": [], "9":[] }
    for root, dirs, files in os.walk(data_set_dir):
        for file in files:
            file_path = root + file 
            number_class = file[0]
            img_path_dict[number_class].append(file_path)
            hamming_dis = Compared_2img_With_hamming(file_path, img_path)
            per_img_hamming_distance[number_class].append(hamming_dis)
    for key, value in per_img_hamming_distance.items():
        print(key, sum(value) / len(value))
    print("--------------------------")





if __name__ == "__main__":
    data_set_dir_0 = "C:/Users/Super/Documents/Captcha/image_0/class/"
    data_set_dir_1 = "C:/Users/Super/Documents/Captcha/image_1/class/"
    data_set_dir_2 = "C:/Users/Super/Documents/Captcha/image_2/class/"
    data_set_dir_3 = "C:/Users/Super/Documents/Captcha/image_3/class/"
    ImageRecognize(data_set_dir_0, "./index_0.jpg")
    ImageRecognize(data_set_dir_1, "./index_1.jpg")
    ImageRecognize(data_set_dir_2, "./index_2.jpg")
    ImageRecognize(data_set_dir_3, "./index_3.jpg")
    # Downloads images and save it to current path 
    url = "https://course.fcu.edu.tw/validateCode.aspx"
    DownloadsImageFromWeb(url = url, count = 1)
    
    # After Downloads Images we split it to 4 slice
    image_path = "./0.jpg"
    Split_Captcha(image_path = image_path, save_dir = "./")
    print("[*] Finish Split Captcha in 4 slice")








