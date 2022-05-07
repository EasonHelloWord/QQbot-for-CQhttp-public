def pictures():
    import random
    import requests
    list = ['美女','爱情','风景','清新','动漫','明星','萌宠','游戏','汽车','时尚','日历','影视','军事','体育','萌娃','格言']
    type = random.choice(list)
    r = requests.get('http://api.wpbom.com/api/picture.php?msg='+type)
    all = r.text
    mes = "随机到了“"+type+"”分类哦："+"[CQ:image,file="+str(all)+"]"
    return mes

