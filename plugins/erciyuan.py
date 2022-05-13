def erciyuan(messages):
    import random
    import requests
    url = ['https://www.dmoe.cc/random.php']
    url = random.choice(url)
    url = requests.get(url)
    all = url.url
    mes = messages["二次元"]+"[CQ:image,file="+all+"]"
    return mes
