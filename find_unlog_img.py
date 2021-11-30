import os 

if __name__ == "__main__":
    all_imgs = os.listdir("./image/")
    
    imgs = os.listdir("./image/class/")
    for per_img in imgs:

        per_img = per_img.split(".")[0]
        per_img_class = per_img[0]
        per_img_name = per_img[1:]
        per_img_file = per_img_name + ".jpg"
        if per_img_file in all_imgs:
            all_imgs.remove(per_img_file)
    
    un_log_imgs = all_imgs
    print(len(un_log_imgs))
       


    






