def send_msg(type,uid,messenge):
    import json
    import requests
    msg = messenge.replace(" ", "%20")
    msg = msg.replace("\n", "%0a")
    msg = msg.replace("&#91;","[").replace("&#93;","]")
    if msg == "":
        msg = "空"
    if type == 'group':
        url = "http://127.0.0.1:5700/send_group_msg?group_id=" + str(uid) + "&message=" + msg
        print("发送"+url)
        r = requests.get(url)
        last = json.loads(r.text)
        last = last['data']
        groupmessageid = last['message_id']
        return groupmessageid

    elif type == 'private':
        url = "http://127.0.0.1:5700/send_private_msg?user_id=" + str(uid) + "&message=" + msg
        print("发送"+url)
        r = requests.get(url)
        last = json.loads(r.text)
        last = last['data']
        qrivatemessageid = last['message_id']
        return qrivatemessageid