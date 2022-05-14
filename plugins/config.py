import os
if not os.path.exists("配置"):#如果没有地址则创建
    os.mkdir("配置")

def config_read(type,uid):
    import json,time
    os.chdir("配置")
    if type == "private":
        filename = "p"+str(uid)+'.json'
    if type == "group":
        filename = "g"+str(uid)+'.json'
    try:
        f = open(filename,encoding = "utf-8")
    except:
        basic = {}
        json.dump(basic,open(filename,'w'),indent=4)
        time.sleep(0.1)
        f=open(str(filename),"a",encoding='utf-8')
    data = f.read()
    f.close
    os.chdir('..')
    return data

def config_change(type,uid,name,detail):
    import json,time
    os.chdir("配置")
    if type == "private":
        filename = "p"+str(uid)+'.json'
    if type == "group":
        filename = "g"+str(uid)+'.json'
    try:
        f = open(filename,encoding = "utf-8")
    except:
        basic = {}
        json.dump(basic,open(filename,'w'),indent=4,ensure_ascii=False)
        time.sleep(0.1)
        f=open(str(filename),encoding='utf-8')
    data = json.loads(f.read())
    f.close
    data[name] = detail
    json.dump(data,open(filename,'w',encoding='utf-8'),indent=4,ensure_ascii=False)
    os.chdir('..')
    return data