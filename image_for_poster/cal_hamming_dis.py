from color_anal import Compared_2img_With_hamming



if __name__ == "__main__":
    BM_img_path = "c:/users/super/documents/topic/image/00000_digit1_gray.jpg"
    Be_tested_img_path = "./00215_gray.jpg"
    h = Compared_2img_With_hamming(BM_img_path, Be_tested_img_path)
    print(h)
