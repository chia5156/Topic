import cv2 
import numpy as np



if __name__ == "__main__":
    # Loads Image 
    img_path = "./test_1.jpg"
    img = cv2.imread(img_path)
    gray_of_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    # Save gray's img
    cv2.imwrite("./gray_of_test_1.jpg", gray_of_img)
    print(gray_of_img)
    # Get mean of gray
    mean_of_gray = np.average(gray_of_img)
    gray_of_img[gray_of_img < mean_of_gray] = 1
    gray_of_img[gray_of_img >= mean_of_gray] = 0
    print(gray_of_img)
    # print average of gray
    print("average value: %s" %(mean_of_gray))
