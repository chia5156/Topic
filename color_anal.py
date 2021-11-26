import cv2 
import time 
import numpy as np
import csv
l = []
def Compared_2img_With_hamming(BM_img_path, be_tested_img_path):
    # Step1. Loads two Images
    # Step2. Simplify colors (Gray scale
    # Step3. Compute each mean of the Gray scale's img
    # Step4. Compare per GrayScale value to mean, use below's rule 
    #        if the value < mean change it to 0
    #        if the value >= mean change it to 1 

    # Loads BM (BenchMark) image
    BM_img = cv2.imread(BM_img_path)    
    gray_of_BM_img = cv2.cvtColor(BM_img, cv2.COLOR_BGR2GRAY)
    mean_of_gray_BM_img = np.average(gray_of_BM_img)
    gray_of_BM_img[gray_of_BM_img < mean_of_gray_BM_img] = 1
    gray_of_BM_img[gray_of_BM_img >= mean_of_gray_BM_img] = 0
    
    # Loads be tested image
    be_tested_img = cv2.imread(be_tested_img_path)
    gray_of_tested_img = cv2.cvtColor(be_tested_img, cv2.COLOR_BGR2GRAY)
    mean_of_tested_img = np.average(gray_of_tested_img)
    gray_of_tested_img[gray_of_tested_img < mean_of_tested_img] = 1
    gray_of_tested_img[gray_of_tested_img >= mean_of_tested_img] = 0 
    
    # Tested image will be benchmarked against to the BM_img  with Hamming distance 
    hamming_distance = len(np.argwhere(gray_of_BM_img != gray_of_tested_img))
    
    return hamming_distance

num = 0 
def Find_Similar_Image(bm_img_path, be_tested_img_path, save_dir, measurement_error):

    hamming_distance = Compared_2img_With_hamming(bm_img_path, be_tested_img_path)
    if hamming_distance < measurement_error:
        print(hamming_distance)
        global num 
        num = num + 1
        # 漢明距離如果小於所設定的測量誤差，就認定被比對的圖片為相似圖片
        img = cv2.imread(be_tested_img_path)
        img_name = be_tested_img_path.split("/")[-1]
        save_path = save_dir + img_name
        cv2.imwrite(save_path, img)
    else:
        #print(hamming_distance)
        pass
    
if __name__ == "__main__":
    count = 10000
    bm_img_path = "./image/00083.jpg" # 1的圖像
    
    for index in range(count):
        be_tested_img_path = "./image/%s.jpg" %(str(index).zfill(len(str(count))))
        Find_Similar_Image(bm_img_path, be_tested_img_path, 13)
    print(num)





















    """
    file_dir = "./"
    file_name = "00001.jpg"
    file_path = file_dir + file_name
    scanner(file_path, )
    """







    """
    file_dir = "./"
    file_name = "00001.jpg"
    file_path = file_dir + file_name

    image = cv2.imread(file_path)
    # Simplify colors 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    # Compute thg average value of gray scale 
    mean_of_grayscale= np.average(gray)
    
    # Compare per Grayscale's value to mean 
    
    - The rule of the comparison 
    - If the value >= means mark it to 0
    - If the value < means mark it to 1
    

    gray[gray < mean_of_grayscale] = 1
    gray[gray >= mean_of_grayscale] = 0
    print(gray)
    
    # Compute the Hamming distance to other picture
    """
