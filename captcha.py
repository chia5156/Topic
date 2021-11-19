from PIL import Image, ImageDraw, ImageFont
from random import randint 

def DrawMosaicOnImage(image, count):
    
    # Generate 1x1 Mosaic and paste it with random mode 
    
    """ Set the Parameter of Mosaic """
    mosaic_size = (1, 1)
    mosaic_color = (0, 0, 0, 50)

    for index in range(count):
        mosaic = Image.new("RGBA", mosaic_size, mosaic_color)
        location = (randint(0, 48), randint(0, 22))
        image.paste(mosaic, location)

def DrawZeroOnImage(image):
    # 8 x 12
    RGBA_mode = "RGBA"
    size = (8, 12)
    blank_image = Image.new(RGBA_mode, (8, 12))
    block = (1, 1)
    for layer in range(13):
        if layer == 0 :
            for color_location in [(3, 0), (4, 0), (5, 0), (6, 0)]:
                block = Image.new(RGBA_mode, (1, 1), (0, 0, 0, 255))
                image.paste(block, color_location)
                image.show()

            # [(3, 0), (4, 0), (5, 0), (6, 0)] layer One
            # [(2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
            # [(1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2)]
            # [(1, 3), (2, 3), (6, 3), (7, 3)]
            # [(1, 4), (6, 4), (7, 4)]
            # [(1, 5), (6, 5), (7, 5)]
            # [(1, 6), (6, 6)]
            # [(1, 7), (6, 7)]
            # [(1, 8), (6, 8)]
            # [(1, 9), (5, 9)]
            # [(1, 10), (2, 10), (3, 10), (4, 10), (5, 10)]
            # [(2, 11), (3, 11), (4, 11)]

            

        elif layer == 0:
            for color_location in [(3, 0), (4, 0), (5, 0), (6, 0)] :
                block = Image.new(RGBA_mode, (1, 1), (0, 0, 0, 255))
                image.paste(block, color_location)
                image.show()
        elif layer == 1:
            for color_location in [(2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]:
                block = Image.new(RGBA_mode, (1, 1), (0, 0, 0, 255))
                image.paste(block, color_location)
                image.show()
        elif layer == 2:
            for color_location in [(1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2)]:
                block = Image.new(RGBA_mode, (1, 1), (0, 0, 0, 255))
                image.paste(block, color_location)
                image.show()
        elif layer == 3:
            for color_location in [(1, 3), (2, 3), (6, 3), (7, 3)]:
                block = Image.new(RGBA_mode, (1, 1), (0, 0, 0, 255))
                image.paste(block, color_location)
                image.show()
        elif layer == 4:
            for color_location in [(1, 4), (6, 4), (7, 4)]:
                block = Image.new(RGBA_mode, (1, 1), (0, 0, 0, 255))
                image.paste(block, color_location)
                image.show()
        elif layer == 5:
            for color_location in [(1, 5), (6, 5), (7, 5)]:
                block = Image.new(RGBA_mode, (1, 1), (0, 0, 0, 255))
                image.paste(block, color_location)
                image.show()
        elif layer == 6:
            for color_location in [(1, 6), (6, 6)]:
                block = Image.new(RGBA_mode, (1, 1), (0, 0, 0, 255))
                image.paste(block, color_location)
                image.show()
        elif layer == 7:
            for color_location in [(1, 7), (6, 7)]:
                block = Image.new(RGBA_mode, (1, 1), (0, 0, 0, 255))
                image.paste(block, color_location)
                image.show()
        elif layer == 8:
            for color_location in [(1, 8), (6, 8)]:
                block = Image.new(RGBA_mode, (1, 1), (0, 0, 0, 255))
                image.paste(block, color_location)
                image.show()
        elif layer == 9:
            for color_location in  [(1, 9), (5, 9)]:
                block = Image.new(RGBA_mode, (1, 1), (0, 0, 0, 255))
                image.paste(block, color_location)
                image.show()
        elif layer == 10:
            for color_location in  [(1, 10), (2, 10), (3, 10), (4, 10), (5, 10)]:
                block = Image.new(RGBA_mode, (1, 1), (0, 0, 0, 255))
                image.paste(block, color_location)
                image.show()
        elif layer == 11:
            for color_location in  [(2, 11), (3, 11), (4, 11)]:
                block = Image.new(RGBA_mode, (1, 1), (0, 0, 0, 255))
                image.paste(block, color_location)
                image.show()
        else:
            print("Hello world")
        





if __name__ == "__main__":
    i = Image.new("RGBA", (8, 12), (0, 0, 0, 0))
    DrawZeroOnImage(i)

    """
    size = (50, 22)
    frame_size = (48, 22)
    #captcha = Image.new("RGBA", (50, 22), (0, 0, 0, 23))
    main_image = Image.new("RGBA", (48, 20), (0, 0, 0, 0))

    main_image.show()
    
    DrawMosaicOnImage(main_image, 500)

    main_image.show()

    #captcha.paste(blank_image, (1, 1))

   # captcha.show()

   

    
    #captcha.show()
    """


















