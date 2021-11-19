import os
from runshell import runshell 
import time
def DownloadsImageFromWeb(url, count):

    # The default save path is working path
    
    for index in range(count):
        file_name = str(index).zfill(len(str(count)))
        output = runshell("curl %s -o %s.jpg" %(url, file_name))
        time.sleep(2)
        print("[%s] Success Downloads" %(file_name))



if __name__ == "__main__":
    url = "https://course.fcu.edu.tw/validateCode.aspx"
    count = 10000
    DownloadsImageFromWeb(url, count)


