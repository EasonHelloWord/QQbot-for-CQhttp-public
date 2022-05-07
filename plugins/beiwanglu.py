def beiwangluread(type,uid):
    import os
    uid = str(uid)
    if not os.path.exists("备忘录"):#如果没有地址则创建
        os.mkdir("备忘录")
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

    except IOError:
        os.chdir("..")
        return("您还没有过备忘录哦！使用帮助输入《备忘录help》")



def beiwangluadd(type,uid,user,mes):
    import os
    if not os.path.exists("备忘录"):#如果没有地址则创建
        os.mkdir("备忘录")
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
    return "保存成功，通过：《备忘录》查看哦！"

def beiwangludel(type,linest,uid):
    import os
    uid = str(uid)
    if not os.path.exists("备忘录"):#如果没有地址则创建
        os.mkdir("备忘录")
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
            with open(uid+".txt", 'r',encoding='utf-8') as f:
                for line in f:
                    if count == linest:
                        print("",end="")
                    else:
                        data = data + line
                    count = count+1
            f.close
            with open(uid+".txt", 'w',encoding='utf-8') as f:
                f.write(data)
        os.chdir("..")
        return "操作成功！"
    except IOError:
        os.chdir("..")
        return("您似乎还没有过备忘录！使用帮助输入《备忘录help》")
