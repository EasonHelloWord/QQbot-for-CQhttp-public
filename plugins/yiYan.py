def yiYan():
    import json
    import requests
    r = requests.get('https://v1.hitokoto.cn/')
    all = r.text
    ku = json.loads(all)
    content = list(ku.values())
    last = content[2]+"   ----"+content[4]
    return last