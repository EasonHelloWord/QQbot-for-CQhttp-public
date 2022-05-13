import os
if not os.path.exists("树洞"):#如果没有地址则创建
    os.mkdir("树洞")

def hollow(msg,messages):
    msg = msg.replace("\r\n", "\r")
    import time
    os.chdir("树洞")
    name = time.strftime("%Y-%m-%d.%H-%M-%S.txt")
    with open(str(name),"a",encoding='utf-8') as f:
        f.write(msg)
    f.close
    os.chdir('..')
    re = readfile(messages)
    return(messages["树洞_保存"]+re)

def readfile(messages):
    import os
    import random
    file_name_list = os.listdir('树洞')

    # 转为转为字符串
    file_name = str(file_name_list)

    # replace替换"["、"]"、" "、"'"
    file_name = file_name.replace("[", "").replace("]", "").replace("'", "").replace(",", "\n").replace(" ", "")
    filename = random.choice(file_name.split())
    os.chdir("树洞")
    f = open(filename,encoding = "utf-8")
    data = f.read()
    f.close
    os.chdir('..')
    return messages["树洞_回复"].format(filename[:-4],data)