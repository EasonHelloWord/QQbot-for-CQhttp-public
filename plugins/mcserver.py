def mcserver(ip,messages,mode='interenet',more='null'):
    from mcstatus import MinecraftServer

    server = MinecraftServer.lookup(ip)
    try:
        if mode == "try":
            try:
                status = server.status()
                return "true"
            except:
                return"false"

        if mode == "local":
            status = server.status()
            latency = server.ping()
            query = server.query()

            mes = messages["服务器_本地_连接"].format(status.players.online, status.latency,latency,", ".join(query.players.names))
            return mes
        if mode == "interenet":
            status = server.status()
            if more == "local":
                return messages["服务器_本地_测试"].format(status.latency)
            else:
                return messages["服务器_网络_测试"].format(status.players.online, status.latency)
    except:
        return messages["服务器_error"]