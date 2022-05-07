def mcserver(ip,mode='interenet',more='null'):
    from mcstatus import MinecraftServer

    server = MinecraftServer.lookup(ip)
    try:
        if mode == "local":
            status = server.status()
            latency = server.ping()
            query = server.query()

            mes = "服务器 {0} 玩家在线，本地连接耗时 {1} ms".format(status.players.online, status.latency)+"\n服务器本地响应时间 {0} ms".format(latency)+"\n在线玩家：{0}".format(", ".join(query.players.names))
            return mes
        if mode == "interenet":
            status = server.status()
            if more == "local":
                return "公网连接耗时 {0} ms".format(status.latency)
            else:
                return "服务器 {0} 玩家在线，连接耗时 {1} ms".format(status.players.online, status.latency)
    except IOError:
        return "服务器似乎未正常启动！"