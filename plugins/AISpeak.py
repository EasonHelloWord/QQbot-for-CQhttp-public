from plugins.send_msg import *
def AISpeak(msg,owner,uid,user):
    import json
    import requests
    r = requests.get('http://api.qingyunke.com/api.php?key=free&appid=0&msg='+msg)
    all = r.text
    ku = json.loads(all)
    content = list(ku.values())
    last = content[1]
    errow_list = ["傻逼","贱人","傻B","牛子","你妹","女优"]
    for x in errow_list:
        if x in last:
            uid,user = str(uid),str(user)
            a = send_msg('private',owner,'截取非法回执：'+last)
            a = str(a)
            send_msg('private',owner,'信息码：'+a+"\nuid:"+uid+"  user:"+user)
            return "非法回执，已自动屏蔽~\n如有异议请向"+owner+"申诉\n信息码："+a
    else:
        last = last.replace("{br}","%0a")
        return last
