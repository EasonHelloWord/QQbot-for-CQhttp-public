def box(message,uid,user,owner):
    import os
    import time
    if not os.path.exists("意见箱"):#如果没有地址则创建
        os.mkdir("意见箱")
    os.chdir("意见箱")
    name = time.strftime("%Y-%m-%d %H-%M-%S.txt")
    with open(str(name),"a",encoding='utf-8') as f:
        f.write("uid:"+uid+"  user:"+user+"\n"+message)
    f.close
    os.chdir('..')
    msg2 = '收到一条来自uid='+uid+'  user='+user+'的建议，详情见意见箱！\n'+message
    return("内容已经转告"+owner+"啦~\n详细信息："+message+"\n由临时会话发起的意见箱"+owner+"可能不会第一时间知道哦~",msg2)
