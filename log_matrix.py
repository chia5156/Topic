from color_anal import Compared_2img_With_hamming
import cv2 
BM_img_path = "C:/Users/Super/Documents/Captcha/image_0/00000.jpg"
Be_tested_img_path = "C:/Users/Super/Documents/Captcha/image_0/00001.jpg"

if __name__ == "__main__":
    ham_distance = Compared_2img_With_hamming(BM_img_path, Be_tested_img_path)


