import cv2 
import time 
import numpy as np
import csv
l = []
def Find_Similar_Image(BM_img_path, be_tested_img_path):
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
    global l
    l.append(hamming_distance)
    return hamming_distance

if __name__ == "__main__":
    # Log the hamming distance which is generate by function to the csv file 
    save_path = "./log.csv"
    logcsv = open(save_path, "w", encoding = "utf8", newline = '')

    count = 10000
    for bm_index in range(count):
        for tested_index in range(count):
            bm_img_path = "./" + str(bm_index).zfill(len(str(count))) + ".jpg"
            be_tested_img_path = "./" + str(tested_index).zfill(len(str(count))) + ".jpg"
            hamming_distance = Find_Similar_Image(bm_img_path, be_tested_img_path)
            log = [bm_img_path, be_tested_img_path, str(hamming_distance)]
            print(bm_img_path + be_tested_img_path + str(hamming_distance))
            writer = csv.writer(logcsv)
            writer.writerow(log)
    
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
