def messageId(num):
    import json
    import requests
    r = requests.get('http://127.0.0.1:5700/get_msg?message_id='+str(num))
    print("获取："+'http://127.0.0.1:5700/get_msg?message_id='+str(num))
    all = r.text
    ku = json.loads(all)
    last = ku["data"]["message"]
    return last