import cv2
from PIL import Image, ImageDraw, ImageFont
if __name__ == "__main__":
    black_block = Image.new("RGBA", (1, 1), (0, 0, 0, 190))
    
    img = Image.open("./00001.jpg")
    img.paste(black_block, (7, 5))
    img.paste(black_block, (13, 5))
    img.paste(black_block, (13, 16))
    img.show()
    

    
