import cv2 
import time 
import numpy as np

def Split_Image(image_path, row_start, row_stop, col_start, col_stop):
        # Get the ROI (Region Of Image) using Numpy indexing
        image = cv2.imread(image_path)
        ROI = image[row_start: row_stop, col_start: col_stop]
        k = cv2.waitKey(0)
        return ROI
def Split_Captcha(image_path, save_dir):
    ROI = Split_Image(image_path, 5, 17, 7, 14)
    cv2.imwrite(save_dir + "index_0.jpg", ROI)
    ROI = Split_Image(image_path, 5, 17, 15, 22)
    cv2.imwrite(save_dir + "index_1.jpg", ROI)
    ROI = Split_Image(image_path, 5, 17, 25, 32)
    cv2.imwrite(save_dir + "index_2.jpg", ROI)
    ROI = Split_Image(image_path, 5, 17, 34, 41)
    cv2.imwrite(save_dir + "index_3.jpg", ROI)

if __name__ == "__main__":
    
    file_dir = "./"
    file_name = "00013.jpg"
    file_path = file_dir + file_name


    # Reading an image from file using cv.imread() 
    image = cv2.imread(file_path)
    # Get Rows and Columns and Channel 
    (row, column) = image.shape[:2]
    # Row six 
    row_5 = image[5]

    def Remove_White_And_Gray_FromRow(row):
        index_of_white = []
        index_of_gray = []
        for index in range(len(row)):
            per_rgb = row[index]
            per_r_value = per_rgb[0]
            per_g_value = per_rgb[1]
            per_b_value = per_rgb[2]
            if (per_r_value == 255 and per_g_value ==255 and per_b_value ==255):
                index_of_white.append(index)

            if (per_r_value == 192 and per_g_value ==192 and per_b_value ==192):
                index_of_gray.append(index)
        index_of_white_and_gray = sorted(index_of_white + index_of_gray)
        without_white_and_gray = np.delete(row, index_of_white_and_gray, axis= 0)
        return without_white_and_gray

    def Split_Image(image_path, row_start, row_stop, col_start, col_stop):
        # Get the ROI (Region Of Image) using Numpy indexing
        image = cv2.imread(image_path)
        ROI = image[row_start: row_stop, col_start: col_stop]
        k = cv2.waitKey(0)
        return ROI
    

    for index in range(10000):
        file_dir = "./"
        file_name = str(index).zfill(len("10000")) + ".jpg"
        file_path = file_dir + file_name
        #ROI = Split_Image(file_path, 5, 17, 7, 14)
        #cv2.imwrite("./image/" + file_name, ROI)
        #ROI = Split_Image(file_path, 5, 17, 15, 22)
        #cv2.imwrite("./image_1/" + file_name, ROI)
        #ROI = Split_Image(file_path, 5, 17, 25, 32)
        #cv2.imwrite("./image_2/" + file_name, ROI)
        ROI = Split_Image(file_path, 5, 17, 34, 41)
        cv2.imwrite("./image_3/" + file_name, ROI)

        

    """
    i = image[5:17, 7:14]
    res = cv2.resize(i, None, fx=10, fy=10)
    cv2.imshow("window", res)
    k = cv2.waitKey(0)
    """
