def haogan_read(uid):
    import os,json
    if not os.path.exists("好感"):#如果没有地址则创建
        os.mkdir("好感")
    os.chdir("好感")
    name = str(uid)+".txt"
    try:
        f = open(name)
    except:
        os.chdir('..')
        return "null"
    js = f.read()
    f.close
    dic = json.loads(js)
    os.chdir("..")
    return dic

def haogan_add(uid,addition=0):
    import os,time,json
    timeNow = time.strftime("%Y-%m-%d.%H-%M-%S")
    addition = int(addition)
    if not os.path.exists("好感"):#如果没有地址则创建
        os.mkdir("好感")
    os.chdir("好感")
    name = str(uid)+".txt"
    if not os.path.exists(name):
        basic = {'haogan':0,"CreateTime":timeNow}
        json.dump(basic,open(name,'w'),indent=4)
        time.sleep(0.1)
    f = open(name)
    js = f.read()
    f.close
    dic = json.loads(js)
    dic['haogan'] = dic['haogan']+addition
    json.dump(dic,open(name,'w'),indent=4)
    os.chdir('..')


def haogan_add_mode(uid,mode,time,addition=0):#制作中
    import os,time,json
    timeNow = time.strftime("%Y-%m-%d.%H-%M-%S")
    addition = int(addition)
    if not os.path.exists("好感"):#如果没有地址则创建
        os.mkdir("好感")
    os.chdir("好感")
    name = str(uid)+".txt"
    if not os.path.exists(name):
        basic = {'haogan':0,"CreateTime":timeNow}
        json.dump(basic,open(name,'w'),indent=4)
        time.sleep(0.1)
    f = open(name)
    js = f.read()
    f.close
    dic = json.loads(js)
    dic['haogan'] = dic['haogan']+addition
    json.dump(dic,open(name,'w'),indent=4)
    os.chdir('..')