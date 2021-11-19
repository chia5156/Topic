from runshell import runshell

if __name__ == "__main__":
    count = 10000
    
    for index in range(10000):
        runshell("mv ./%s.jpg ./captcha/%s.jpg" %(str(index).zfill(len(str(10000))), str(index).zfill(len(str(10000)))))

    
