def erciyuan():
    import random
    import requests
    url = ['https://www.dmoe.cc/random.php']
    url = random.choice(url)
    url = requests.get(url)
    all = url.url
    mes = "二次元来喽~~"+"[CQ:image,file="+all+"]"
    return mes
