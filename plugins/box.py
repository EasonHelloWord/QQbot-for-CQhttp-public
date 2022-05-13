import os
if not os.path.exists("意见箱"):#如果没有地址则创建
    os.mkdir("意见箱")

def box(message,uid,user,owner,messages):
    import time
    os.chdir("意见箱")
    name = time.strftime("%Y-%m-%d %H-%M-%S.txt")
    with open(str(name),"a",encoding='utf-8') as f:
        f.write("uid:"+uid+"  user:"+user+"\n"+message)
    f.close
    os.chdir('..')
    msg2 = messages["意见箱_owner"].format(uid,user,message)
    return(messages["意见箱_private"].format(owner,message,owner),msg2)
