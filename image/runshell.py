import os 


DirectoryPath = "C:/Users/wei/build/application/"
NoxDirectory = "D:/program files/Nox/bin/"



def runshell(*argvs):
    
    try:
        ResultObject = os.popen(argvs[0])
        
        return ResultObject

    except Exception as e:
       error_class = e.__class__.__name__ #取得錯誤類型
       detail = e.args[0] #取得詳細內容
       cl, exc, tb = sys.exc_info() #取得Call Stack
       lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
       fileName = lastCallStack[0] #取得發生的檔案名稱
       lineNum = lastCallStack[1] #取得發生的行號
       funcName = lastCallStack[2] #取得發生的函數名稱
       errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
       print(errMsg)


def Get_Symbol_Table(FilePath, ):
    # Use objdump command with -T optinals to get the symbol table 

    result_object = runshell("objdump -T " + FilePath)
    
    output = result_object.readlines()

    for index in range(len(output)):
        print(output[index].rstrip("\n"))

    print(len(output))
    


