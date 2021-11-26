import color_anal
import os 

def Get_all_files(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(file)
    return file_list
def Inspect_img(img_1_path, img_2_path):
    h = color_anal.Compared_2img_With_hamming(img_1_path, img_2_path)
    if (h == 0) and (img_1_path != img_2_path):
        print("[*]%s, %s" %(img_1_path, img_2_path))
    else:
        pass
if __name__ == "__main__":
    file_dir = "C:/Users/Super/Documents/Topic/image/class/"
    l = Get_all_files("C:/Users/Super/Documents/Topic/image/class/")
    for index in range(len(l)):
        for index_2 in range(len(l)):
            Inspect_img(file_dir + l[index], file_dir + l[index_2])

        
