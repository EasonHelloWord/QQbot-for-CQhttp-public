def answer_from_ciku(mes,uid):
    from plugins.haogan import haogan_read
    import os
    if not os.path.exists("词库"):#如果没有地址则创建
        os.mkdir("词库")
    os.chdir("词库")
    name = mes+".txt"
    os.chdir("..")
    haogan = haogan_read(uid)['haogan']
    haogan = int(haogan)
    if haogan <=-10:
        qujian='-3'
    if -10 < haogan <=-5:
        qujian ='-2'
    if -5 < haogan <=-2:
        qujian ='-1'
    if -2 < haogan <= 2:
        qujian = '0'
    if 2<haogan<=5:
        qujian='1'
    if 5<haogan<=10:
        qujian='2'
    if haogan>10:
        qujian='3'
    print(qujian)


from plugins.send_msg import *
def AISpeak(msg,owner,uid,user,messages):
    import json
    import requests
    r = requests.get('http://api.qingyunke.com/api.php?key=free&appid=0&msg='+msg)
    all = r.text
    ku = json.loads(all)
    content = list(ku.values())
    last = content[1]
    errow_list = messages["青云客_屏蔽词_list"]
    for x in errow_list:
        if x in last:
            uid,user = str(uid),str(user)
            a = send_msg('private',owner,messages["青云客_屏蔽_owner"].format(last))
            a = str(a)
            send_msg('private',owner,messages["青云客_屏蔽_owner2"].format(a,uid,user))
            return messages["青云客_屏蔽_private"].format(owner,a)
    else:
        last = last.replace("{br}","%0a")
        return last