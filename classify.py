import color_anal
from runshell import runshell 

if __name__ == "__main__":
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



