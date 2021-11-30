import color_anal
from runshell import runshell 

def classify(bm_img_path_list, tested_img_dir, save_path):
    # bm_img_path_list 自己各自從0到9選出一張作為辨識機準圖片作為代表
    img_class = [str(index) for index in range(10)]
    bm_img_path = [img_path for img_path in bm_img_path_list]
    img_path_dict = dict(zip(img_class, bm_img_path))
    img_count = 10000
    for per_bm_img_index in range(len(img_path_dict)):
        per_bm_img_path = img_path_dict[str(per_bm_img_index)]
        for tested_img_index in range(img_count):
            tested_img_path = tested_img_dir + str(tested_img_index).zfill(len(str(img_count))) + ".jpg"
            save_path = save_path
            color_anal.Find_Similar_Image(per_bm_img_path, tested_img_path, save_path + "%s" %(per_bm_img_index), 13)




if __name__ == "__main__":
    img_dir = "./image_1/"
    l = [img_dir + "00000.jpg", img_dir + "00003.jpg", img_dir + "00009.jpg",\
         img_dir + "00035.jpg", img_dir + "00036.jpg", img_dir + "00005.jpg",\
         img_dir + "00037.jpg", img_dir + "00042.jpg", img_dir + "00043.jpg",\
         img_dir + "00023.jpg"]
    img_2_dir = "./image_2/"
    l_2 = [img_2_dir + "00003.jpg", img_2_dir + "00000.jpg", img_2_dir + "00049.jpg",\
           img_2_dir + "00083.jpg", img_2_dir + "00064.jpg", img_2_dir + "00080.jpg",\
           img_2_dir + "00069.jpg", img_2_dir + "00096.jpg", img_2_dir + "00112.jpg",\
           img_2_dir + "00050.jpg"]
    img_3_dir = "./image_3/"
    l_3 = [img_3_dir + "00005.jpg", img_3_dir + "00032.jpg", img_3_dir + "00007.jpg",\
           img_3_dir + "00008.jpg", img_3_dir + "00052.jpg", img_3_dir + "00010.jpg",\
           img_3_dir + "00024.jpg", img_3_dir + "00037.jpg", img_3_dir + "00055.jpg",\
           img_3_dir + "00051.jpg"]
    #classify(l, img_dir, img_dir + "class/")
    #classify(l_2, img_2_dir, img_2_dir + "class/")
    classify(l_3, img_3_dir, img_3_dir + "class/")
    # log number 0-9's file path with dictionary
    img_path_dict = {"0": "./image/00005.jpg",\
            "1": "./image/00001.jpg",\
            "2": "./image/00028.jpg",\
            "3": "./image/00086.jpg",\
            "4": "./image/00000.jpg",\
            "5": "./image/00145.jpg",\
            "6": "./image/00156.jpg",\
            "7": "./image/00003.jpg",\
            "8": "./image/00014.jpg",\
            "9": "./image/00038.jpg"
            }
    count = 10000
    for bm_img_index in range(len(img_path_dict)):
        runshell("mkdir %s" %(str(bm_img_index)))
        bm_img_path = img_path_dict[str(bm_img_index)]
        for tested_img_index in range(count):
            tested_img_name = str(tested_img_index).zfill(len(str(count)))
            tested_img_path = "./image/%s.jpg" %(tested_img_name)
            color_anal.Find_Similar_Image(bm_img_path, tested_img_path, "./image/class/%s" %(str(bm_img_index)), 13)
