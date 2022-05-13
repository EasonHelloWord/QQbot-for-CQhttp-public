import os
if not os.path.exists("好感"):#如果没有地址则创建
    os.mkdir("好感")

def haogan_read(uid):
    import json
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
    import time,json
    timeNow = time.strftime("%Y-%m-%d.%H-%M-%S")
    addition = int(addition)
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
    import time,json
    timeNow = time.strftime("%Y-%m-%d.%H-%M-%S")
    addition = int(addition)
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