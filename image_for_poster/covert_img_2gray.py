import cv2 
import os 




if __name__ == "__main__":
    img_path = "./00088.jpg"
    img = cv2.imread(img_path)
    i = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print(img_path)
    for root, dirs, files in os.walk("./"):
        file_dir = root
        for file in files:
            file_name = file
            image_path = file_dir + file_name
            print(image_path)
            try:
                image = cv2.imread(image_path)
                gray_of_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                print(gray_of_image)
                numbering_of_file = file_name.split(".")[0]
                format_of_file = file_name.split(".")[-1]
                save_path = file_dir + "%s_gray.%s" %(numbering_of_file, format_of_file)
                cv2.imwrite(save_path, gray_of_image)
            except:
               print("except")
