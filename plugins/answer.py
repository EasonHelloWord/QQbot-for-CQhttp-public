def answer_from_ciku(mes,uid):
    from plugins.haogan import haogan_read
    import os
    if not os.path.exists("词库"):#如果没有地址则创建
        os.mkdir("词库")
    os.chdir("词库")
    name = mes+".txt"
    os.chdir("..")
    haogan = haogan_read(uid)['haogan']
    print(haogan)
