from plugins.AISpeak import *
from plugins.beiwanglu import *
from plugins.box import *
from plugins.erciyuan import *
from plugins.haogan import *
from plugins.hollow import *
from plugins.mcserver import *
from plugins.musicApi import *
from plugins.pictures import *
from plugins.send_msg import *
from plugins.yiYan import *
from flask import Flask, request

app = Flask(__name__)




@app.route('/', methods=["POST"])
def post_data():
    if request.get_json().get('message_type') == 'private':  # 私聊信息
        type = 'private'
        uid = request.get_json().get('sender').get('user_id')  # 获取信息发送者的 QQ号码
        user = uid
        message = request.get_json().get('raw_message')  # 获取原始信息
        send(message, uid, user,type)  # 将 Q号和原始信息传到我们的后台

    if request.get_json().get('message_type') == 'group':  # 如果是群聊信息
        message = request.get_json().get('raw_message')  # 获取原始信息
        if message[0] ==".":
            message = message[1:]
            type = 'group'
            uid = request.get_json().get('group_id')  # 获取群号
            user = request.get_json().get('sender').get('user_id')  # 获取信息发送者的 QQ号码
            send(message, uid,user,type)  # 将 Q号和原始信息传到我们的后台
        else:
            type = 'group'
            uid = request.get_json().get('group_id')  # 获取群号
            user = request.get_json().get('sender').get('user_id')  # 获取信息发送者的 QQ号码
            send2(message, uid,user,type)


    return "None"


def send(message, uid, user,type):
    cases = '_'
    if message == '？':
        cases = 3
    if message == '测试':
        cases = 1
    if message == '简介':
        cases = 2
    if message == '一言':
        cases = 4
    if message[0] == '说':
        cases = 5



    if '夸我' in message:
        cases = 8
    if message == '听音乐':
        cases = 9
    if message == '看图片':
        cases = 10
    if message[0:3] == '意见箱':
        cases = 11
    if message[0:2] == '树洞':
        cases = 12




    if message == "二次元":
        cases = 15
    if message[:2] == "刷屏":
        cases = 16
    if message[:4] == "send":
        cases = 17
    if message =="清理缓存":
        cases = 18
    if message[:3] == "服务器":
        cases=19
    if message == "qwq":
        cases = 20
    if message[:3] == "备忘录":
        cases = 21
    if message[0] == ".":
        cases = 'null'


    match cases:
        # 固定格式
        case 'null':
            pass
        case 1:
            send_msg(type,uid,'机器人在线~')
        case 2:
            send_msg(type,uid,'本机器人由Eason_J出版！\n使用流行的go-cqhttp内核，内核版本：v1.0.0-rc1\n文件版本：0.10\n最后更新：不知道qwq')
        case 3:
            send_msg(type,uid,'目前支持的指令有：测试、？、简介、一言、说、听音乐、看图片、二次元、意见箱、树洞、备忘录、服务器\n群聊下请在每句话句首加入<.>，私聊则不用~')





        # 多功能
        case 4:
            msg = yiYan()
            send_msg(type,uid,msg)


        case 5:
            msg = message[1:]
            if msg == "":
                send_msg(type,uid,'请在说后面加入要说的话哦，就像这样\n说你好')
            else:
                send_msg(type,uid,'[CQ:tts,text='+msg+']')





        case 8:
            user = str(user)
            if user == owner:
                send_msg(type,uid,"主人最棒啦！！！！！")
            else:
                send_msg(type,uid,"你谁啊，不认识你")
            haogan_add(user,-0.3)

        case 9:
            msg = musicApi()
            print(msg)
            send_msg(type,uid,msg)

        case 10:
            msg = pictures()
            send_msg(type,uid,msg)

        case 11:
            msg = message[3:]
            if msg == "":
                send_msg(type,uid,'请在说后面加入要说的话哦，就像这样\n意见箱XXX')
            else:
                uid,user = str(uid),str(user)
                msg,msg2 = box(message[3:],uid,user,owner)
                send_msg(type,uid,msg)
                send_msg('private',owner,msg2)
                haogan_add(user,0.2)
        case 12:
            msg = message[2:]
            if msg == "":
                send_msg(type,uid,'请在说后面加入要说的话哦，就像这样\n树洞XXX')
            else:
                msg= hollow(msg)
                send_msg(type,uid,msg)
                haogan_add(user,0.5)



        case 15:
            msg = erciyuan()
            send_msg(type,uid,msg)
            haogan_add(user,-0.1)


        case 16:
            user = str(user)
            msg1 = "来自："+user+"的刷屏~"
            send_msg(type,uid,msg1)
            number = int(message[3:6])
            sends = message[7:]
            if number > 300:
                send_msg(type,uid,"error:上限最多300条哦!")
            else:
                for x in range(number):
                    send_msg(type,uid,sends)
                    haogan_add(user,-0.01)

        case 17:
            user = str(user)
            if user == owner:
                messagel = str(message)
                listl = messagel.split(",")
                typel = listl[1]
                uidl=listl[2]
                mesl = str(listl[3:])[2:-2]
                mesl = mesl.replace("'",'')
                send_msg(typel,uidl,"收到一条来自"+owner+"的消息："+mesl)
                send_msg(type,uid,"发送成功~")
            else:
                send_msg(type,uid,"只有主人才可以用这个命令哦~")


        case 18:
            os.system('cls')
            send_msg(type,uid ,'缓存清理完成！')



        case 19:
            if message[3:] == "":
                mes = "用法：\n查询已注册服务器：服务器all\n查询其他服务器：服务器查询<ip>\n启动服务器：服务器启动<生存>/<创造>"
                send_msg(type,uid ,mes)
            if message[3:] == "all":
                chuangzao,shencun = str(dic["chuangzao"]),str(dic["shencun"])
                mes = mcserver("127.0.0.1:25565","local")
                mes2 = mcserver(chuangzao,"interenet",'local')
                mesf = str(mes)+"\n"+str(mes2)
                send_msg(type,uid,"创造"+mesf)


                mes = mcserver("127.0.0.1:25566","local")
                mes2 = mcserver(shencun,"interenet",'local')
                mesf = str(mes)+"\n"+str(mes2)
                send_msg(type,uid,"生存"+mesf)




            if message[3:5] == "查询":
                ip = message[5:]
                mes = mcserver(str(ip))
                send_msg(type,uid ,mes)
            if message[3:5] == "启动":
                if message[5:] == "创造":
                    os.system("start chuangzao.bat")
                    send_msg(type,uid,"创造启动成功")
                if message[5:] == "生存":
                    os.system("start shencun.bat")
                    send_msg(type,uid,"生存启动成功")

        case 20:
            import random
            num = random.randint(0,2)
            if num == 1:
                send_msg(type,uid,"qwq")


        case 21:
            mes = message[3:]
            if mes == "":
                data = beiwangluread(type,uid)
            elif mes == "help":
                data = "增加备忘录：备忘录XXX\n读取备忘录：备忘录\n删除备忘录指定行：备忘录删除<行号>\n存档各用户与群聊互不相同。"
            elif mes[:2] == '删除':
                try:
                    linest = int(mes[2:])
                    data = beiwangludel(type,linest,uid)
                except IOError:
                    data = "传入参数错误，使用帮助输入《备忘录help》"
            else:
                data = beiwangluadd(type,uid,user,mes)
            send_msg(type,uid,data)




        case _:
            msg = AISpeak(message,owner,uid,user)
            send_msg(type,uid ,msg)
            # send_msg(type,uid,'未知的命令~，输入help来获取帮助~\n群聊请在文本前加入“.”')


def send2(message, uid, user,type):
    cases = '_'
    if message == 'qwq':
        cases = 1

    match cases:
        case 1:
            import random
            num = random.randint(0,2)
            if num == 1:
                send_msg(type,uid,"qwq")




if __name__ == '__main__':
    import os,json,time
    if not os.path.exists('config.json'):
        basic = {"owner":123123123,"shenucn":"www.www.cn","chuangzao":"www.www.cn"}
        json.dump(basic,open('config.json','w'),indent=4)
        time.sleep(0.1)
        print("配置文件生成完毕，请前往'config.json'完成设置~")
    f = open('config.json')
    js = f.read()
    f.close
    dic = json.loads(js)
    owner = str(dic["owner"])
    app.run(debug=True, host='127.0.0.1', port=5701)  # 此处的 host和 port对应上面 yml文件的设置

