def musicApi(messages):
    import json
    import requests
    r = requests.get('http://api.wpbom.com/api/neran.php')
    all = r.text
    ku = json.loads(all[5:])
    ku = ku['meta']['music']
    type = 'custom'
    url = ku['musicUrl']
    audio = url
    title = messages["音乐_来了"]
    content = messages["音乐_下载"].format(ku['title'],ku['desc'])
    image = ku['preview']
    return('[CQ:music,'+'type='+type+',url='+url+',audio='+audio+',title='+title+',content='+content+',image='+image+']')
