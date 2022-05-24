import os
if not os.path.exists("备忘录"):#如果没有地址则创建
    os.mkdir("备忘录")


def beiwangluread(type,uid,messages):
    uid = str(uid)
    os.chdir("备忘录")
    try:
        if type == 'private':
            data = ""
            count = 1
            with open('p'+uid+".txt", 'r',encoding='utf-8') as f:
                for line in f:
                    c = str(count)
                    data = data+c+line
                    count = count+1
            os.chdir("..")
            return data
        if type == 'group':
            data = ""
            count = 1
            with open(uid+".txt", 'r',encoding='utf-8') as f:
                for line in f:
                    c = str(count)
                    data = data+c+line
                    count = count+1
            os.chdir("..")
            return data

    except:
        os.chdir("..")
        return(messages["备忘录_文件_error"])



def beiwangluadd(type,uid,user,mes,messages):
    os.chdir("备忘录")
    uid,user = str(uid),"、"+str(user)+":"
    mes = mes.replace("\r\n", "%0a")
    if type == "private":
        uid = "p"+uid
        user = "、"
    with open(uid+".txt","a",encoding='utf-8') as f:
        f.write(user+mes+"\n")
    f.close
    os.chdir("..")
    return messages["备忘录_保存"]

def beiwangludel(type,linest,uid,messages,user,owner):
    uid = str(uid)
    os.chdir("备忘录")
    try:
        if type == 'private':
            data = ""
            count = 1
            with open("p"+uid+".txt", 'r',encoding='utf-8') as f:
                for line in f:
                    if count == linest:
                        print("",end="")
                    else:
                        data = data + line
                    count = count+1
            f.close
            with open("p"+uid+".txt", 'w',encoding='utf-8',) as f:
                f.write(data)


        if type == 'group':
            data = ""
            count = 1
            user_leng = len(str(user))
            with open(uid+".txt", 'r',encoding='utf-8') as f:
                for line in f:
                    if count == linest:
                        if str(line[1:user_leng+1]) == str(user):
                            print("",end="")
                        elif str(user) == str(owner):
                            print("",end="")
                        else:
                            os.chdir("..")
                            return(messages["备忘录_!owner"])
                    else:
                        data = data + line
                    count = count+1
            f.close
            with open(uid+".txt", 'w',encoding='utf-8') as f:
                f.write(data)
        os.chdir("..")
        return messages["备忘录_删除"]
    except:
        os.chdir("..")
        return(messages["备忘录_文件_error"])
