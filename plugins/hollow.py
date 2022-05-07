def hollow(msg):
    msg = msg.replace("\r\n", "\r")
    import os
    import time
    if not os.path.exists("树洞"):#如果没有地址则创建
        os.mkdir("树洞")
    os.chdir("树洞")
    name = time.strftime("%Y-%m-%d.%H-%M-%S.txt")
    with open(str(name),"a",encoding='utf-8') as f:
        f.write(msg)
    f.close
    os.chdir('..')
    re = readfile('树洞')
    return("内容保存成功，不会记录您的信息哦~\n"+re)

def readfile(filedata):
    import os
    import random
    file_name_list = os.listdir(filedata)

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
    return "来自时间："+filename[:-4]+"的树洞：\n"+data