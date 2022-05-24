from plugins.answer import *
from plugins.beiwanglu import *
from plugins.box import *
from plugins.config import *
from plugins.dinshizhixing import *
from plugins.erciyuan import *
from plugins.haogan import *
from plugins.hollow import *
from plugins.mcserver import *
from plugins.messageId import *
from plugins.musicApi import *
from plugins.pictures import *
from plugins.send_msg import *
from plugins.yiYan import *
from flask import Flask, request

app = Flask(__name__)




@app.route('/', methods=["POST"])
def post_data():
    dinshixiaoxi(temp,config,messages)
    # print(request.get_json())
    if request.get_json().get('message_type') == 'private':  # 私聊信息
        type = 'private'
        uid = request.get_json().get('sender').get('user_id')  # 获取信息发送者的 QQ号码
        user = uid
        message = request.get_json().get('raw_message')  # 获取原始信息
        send(message, uid, user,type)  # 将 Q号和原始信息传到我们的后台

    if request.get_json().get('message_type') == 'group':  # 如果是群聊信息
        message = request.get_json().get("raw_message")  # 获取原始信息
        if message[:KeyWorld_Length] ==KeyWorld:
            message = message[KeyWorld_Length:]
            type = 'group'
            uid = request.get_json().get('group_id')  # 获取群号
            user = request.get_json().get('sender').get('user_id')  # 获取信息发送者的 QQ号码
            send(message, uid,user,type)  # 将 Q号和原始信息传到我们的后台
        else:
            type = 'group'
            uid = request.get_json().get('group_id')  # 获取群号
            user = request.get_json().get('sender').get('user_id')  # 获取信息发送者的 QQ号码
            send2(message, uid,user,type)


    if request.get_json().get('notice_type') == 'group_recall':
        import json
        recall_group_id = request.get_json().get('group_id')
        choose = json.loads(config_read('group',recall_group_id))['un_recall']
        if choose == 'true':
            recall_user_id = request.get_json().get('user_id')
            recall_operator_id = request.get_json().get('operator_id')
            recall_message_id = request.get_json().get('message_id')
            recall_data = [recall_user_id,recall_operator_id,recall_message_id,recall_group_id]
            group_recall(recall_data)

    return "你好"

def group_recall(recall_data):
    recall_message = messageId(recall_data[2])
    send_msg('group',recall_data[3],messages["撤回"].format(recall_data[1],recall_data[0],recall_message))



def group_recall(recall_data):
    recall_message = messageId(recall_data[2])
    send_msg('group',recall_data[3],messages["撤回"].format(recall_data[1],recall_data[0],recall_message))




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

    if message == '初始化':
        cases = 6



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

    if message[0:4] == '定时消息':
        cases = 13




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
    if message[:2] == "配置":
        cases = 22
    if message[0] == ".":
        cases = 'null'


    match cases:
        # 固定格式
        case 'null':
            pass
        case 1:
            send_msg(type,uid,messages["测试"])
        case 2:
            send_msg(type,uid,messages["简介"])
        case 3:
            send_msg(type,uid,messages["？"].format(config["KeyWorld"]))





        # 多功能
        case 4:
            msg = yiYan()
            send_msg(type,uid,msg)


        case 5:
            msg = message[1:]
            if msg == "":
                send_msg(type,uid,messages["说_error"])
            else:
                send_msg(type,uid,'[CQ:tts,text='+msg+']')

        case 6:
            os.system("cd /d "+config["path"])
            chushihua()
            send_msg(type,uid,messages["初始化"])



        case 8:
            user = str(user)
            if user == owner:
                send_msg(type,uid,"主人最棒啦！！！！！")
            else:
                send_msg(type,uid,"你谁啊，不认识你")
            haogan_add(user,-0.3)

        case 9:
            msg = musicApi(messages)
            print(msg)
            send_msg(type,uid,msg)

        case 10:
            msg = pictures(messages)
            send_msg(type,uid,msg)

        case 11:
            msg = message[3:]
            if msg == "":
                send_msg(type,uid,messages["意见箱_error"])
            else:
                uid,user = str(uid),str(user)
                msg,msg2 = box(message[3:],uid,user,owner,messages)
                send_msg(type,uid,msg)
                send_msg('private',owner,msg2)
                haogan_add(user,0.2)
        case 12:
            msg = message[2:]
            if msg == "":
                send_msg(type,uid,messages["树洞_error"])
            else:
                msg= hollow(msg,messages)
                send_msg(type,uid,msg)
                haogan_add(user,0.5)

        case 13:
            send_msg(type,uid,messages["定时消息_help"])

        case 15:
            msg = erciyuan(messages)
            send_msg(type,uid,msg)
            haogan_add(user,-0.1)


        case 16:
            user = str(user)
            msg1 = messages["刷屏"].format(user)
            send_msg(type,uid,msg1)
            number = int(message[3:6])
            sends = message[7:]
            if number > 300:
                send_msg(type,uid,messages["刷屏_error"])
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
                send_msg(typel,uidl,messages["消息_收到"].format(owner,mesl))
                send_msg(type,uid,messages["消息_发送_success"])
            else:
                send_msg(type,uid,messages["消息_发送_error"])


        case 18:
            os.system('cls')
            send_msg(type,uid ,messages["缓存"])



        case 19:
            if message[3:] == "":
                mes = messages["服务器_help"]
                send_msg(type,uid ,mes)
            if message[3:] == "all":
                chuangzao,shencun = str(config["chuangzao"]),str(config["shencun"])
                mes = mcserver("127.0.0.1:25565",messages,"local")
                mes2 = mcserver(chuangzao,messages,"interenet",'local')
                mesf = str(mes)+"\n"+str(mes2)
                send_msg(type,uid,"创造"+mesf)


                mes = mcserver("127.0.0.1:25566",messages,"local")
                mes2 = mcserver(shencun,messages,"interenet",'local')
                mesf = str(mes)+"\n"+str(mes2)
                send_msg(type,uid,"生存"+mesf)




            if message[3:5] == "查询":
                ip = message[5:]
                mes = mcserver(str(ip))
                send_msg(type,uid ,mes)
            if message[3:5] == "启动":
                if message[5:] == "创造":
                    a = mcserver('127.0.0.1:25565',messages,mode='try',more='null')
                    if a =="false":
                            import time
                            timeNow = time.time()
                            try:
                                lasttime = temp['chuangzao']
                                if timeNow-lasttime >= 300:
                                    temp['chuangzao'] = timeNow
                                    os.system("start chuangzao.bat")
                                    send_msg(type,uid,messages["服务器_创造_启动"])
                                else:
                                    send_msg(type,uid,messages["服务器_启动_过快"].format(int(30-timeNow+lasttime)))
                            except:
                                temp['chuangzao'] = timeNow
                                os.system("start chuangzao.bat")
                                send_msg(type,uid,messages["服务器_创造_启动"])
                    else:
                        send_msg(type,uid,messages["服务器_ready"])
                if message[5:] == "生存":
                    a = mcserver('127.0.0.1:25566',messages,mode='try',more='null')
                    if a =="false":
                        import time
                        timeNow = time.time()
                        try:
                            lasttime = temp['shencun']
                            if timeNow-lasttime >= 300:
                                temp['shencun'] = timeNow
                                os.system("start shencun.bat")
                                send_msg(type,uid,messages["服务器_创造_启动"])
                            else:
                                send_msg(type,uid,messages["服务器_启动_过快"].format(int(30-timeNow+lasttime)))
                        except:
                            temp['shencun'] = timeNow
                            os.system("start shencun.bat")
                            send_msg(type,uid,messages["服务器_生存_启动"])
                    else:
                        send_msg(type,uid,messages["服务器_ready"])

        case 20:
            import random
            num = random.randint(0,2)
            if num == 1:
                send_msg(type,uid,"qwq")


        case 21:
            mes = message[3:]
            if mes == "":
                data = beiwangluread(type,uid,messages)
            elif mes == "help":
                data = messages["备忘录_help"]
            elif mes[:2] == '删除':
                try:
                    linest = int(mes[2:])
                    data = beiwangludel(type,linest,uid,messages,user,owner)
                except:
                    data = messages["备忘录_参数_error"]
            else:
                data = beiwangluadd(type,uid,user,mes,messages)
            send_msg(type,uid,data)

        case 22:
            data = message[2:]
            if data == "":
                send_msg(type,uid,messages["配置"])
                send_msg(type,uid,messages["配置2"].format(config_read(type,uid)))
            elif '*'in data:
                key_locate=data.find('*')
                name = data[:key_locate]
                detail = data[key_locate+1:]
                config_change(type,uid,name,detail)
                send_msg(type,uid,messages["配置更改"].format(name,detail))
            else:
                send_msg(type,uid,messages["配置"])
        case _:
            msg = AISpeak(message,owner,uid,user,messages)
            send_msg(type,uid ,msg)
            # send_msg(type,uid,'未知的命令~，输入help来获取帮助~\n群聊请在文本前加入“.”')


def send2(message, uid, user,type):
    cases = '_'
    if message == 'qwq':
        cases = 1
    if  "type=flash" in message:
        cases = 2

    match cases:
        case 1:
            import random
            num = random.randint(0,2)
            if num == 1:
                send_msg(type,uid,"qwq")
        case 2:
            try:
                choose = json.loads(config_read('group',uid))['flash_image']
                if choose == "true":
                    re=message.replace("[","").replace("]","")
                    re = re.split(',')
                    res = "["+re[0]+","+re[1]+"]"
                    send_msg(type,uid,messages["收到闪照"]+res)

            except:pass






def chushihua():
    import os,json,time,socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(("127.0.0.1", int(5701)))
        s.settimeout(1)
        s.shutdown(2)
        print("占用")
        zhanyong = 'true'
    except:
        print("无")
    if not os.path.exists('config.json'):
        basic = {"owner":123123123,"shencun":"www.www.cn","chuangzao":"www.www.cn","KeyWorld":".","path":"C:/asdasdasdasd/sadasdasd"}
        json.dump(basic,open('config.json','w'),indent=4)
        time.sleep(0.1)
        print("配置文件生成完毕，请前往'config.json'完成设置~")
    if not os.path.exists('message.json'):
        basic = {
    "测试": "机器人在线~",
    "简介": "本机器人由Eason_J出版！\n使用流行的go-cqhttp内核，内核版本：v1.0.0-rc1\n文件版本：0.10\n最后更新：不知道qwq",
    "？": "目前支持的指令有：测试、？、简介、一言、说、听音乐、看图片、二次元、意见箱、树洞、备忘录、服务器\n群聊下请在每句话句首加入<{0}>，私聊则不用~",
    "说_error": "请在说后面加入要说的话哦，就像这样\n说你好",
    "意见箱_error": "请在说后面加入要说的话哦，就像这样\n意见箱XXX",
    "意见箱_owner": "收到一条来自uid={0}  user={1}的建议，详情见意见箱！\n{2}",
    "意见箱_private": "内容已经转告{0}啦~\n详细信息：{1}\n由临时会话发起的意见箱{2}可能不会第一时间知道哦~",
    "树洞_error": "请在说后面加入要说的话哦，就像这样\n树洞XXX",
    "树洞_保存": "内容保存成功，不会记录您的信息哦~\n",
    "树洞_回复": "来自时间：{0}的树洞：\n{1}",
    "刷屏": "来自：{0}的刷屏~",
    "刷屏_error": "error:上限最多300条哦!",
    "消息_收到": "收到一条来自{0}的消息：{1}",
    "消息_发送_success": "发送成功~",
    "消息_发送_error": "只有主人才可以用这个命令哦~",
    "缓存": "缓存清理完成！",
    "服务器_help": "用法：\n查询已注册服务器：服务器all\n查询其他服务器：服务器查询<ip>\n启动服务器：服务器启动<生存>/<创造>",
    "服务器_创造_启动": "创造启动成功",
    "服务器_生存_启动": "生存启动成功",
    "服务器_本地_连接": "服务器 {0} 玩家在线，本地连接耗时 {1} ms\n服务器本地响应时间 {2} ms\n在线玩家：{3}",
    "服务器_本地_测试": "公网连接耗时 {0} ms",
    "服务器_网络_测试": "服务器 {0} 玩家在线，连接耗时 {1} ms",
    "服务器_error": "服务器似乎未正常启动！",
    "备忘录_help": "增加备忘录：备忘录XXX\n读取备忘录：备忘录\n删除备忘录指定行：备忘录删除<行号>\n存档各用户与群聊互不相同。",
    "备忘录_参数_error": "传入参数错误，使用帮助输入《备忘录help》",
    "备忘录_文件_error": "您还没有过备忘录哦！使用帮助输入《备忘录help》",
    "备忘录_删除": "操作成功！",
    "备忘录_保存":"保存成功，通过：《备忘录》查看哦！",
    "备忘录_!owner":"您不是这个备忘录的主人！",
    "青云客_屏蔽词_list": [
        "傻逼",
        "贱人",
        "傻B",
        "牛子",
        "你妹",
        "女优",
        "你他妈",
        "几个妹子"
    ],
    "青云客_屏蔽_owner": "截取非法回执：{0}",
    "青云客_屏蔽_owner2":"信息码：{0}\nuid:{1}  user:{2}",
    "青云客_屏蔽_private": "非法回执，已自动屏蔽~\n如有异议请向{0}申诉\n信息码：{1}",
    "二次元": "二次元来喽！！！",
    "音乐_来了": "音乐来喽~~~",
    "音乐_下载": "点击下载哦\n{0}   ---{1}",
    "看图片": "随机到了“{0}”分类哦：",
    "撤回":"震惊！{0}撤回了一条{1}的消息：\n{2}"
    }
        json.dump(basic,open('message.json','w',encoding='utf-8'),indent=4,ensure_ascii=False)
        time.sleep(0.1)
    global temp
    temp = {
        "LaunchNotification":"false"
    }

if __name__ == '__main__':
    import json
    chushihua()

    f = open('config.json')
    js = f.read()
    f.close
    config = json.loads(js)


    f = open('message.json',encoding='utf-8')
    messages = f.read()
    f.close
    messages = json.loads(messages)

    owner = str(config["owner"])
    KeyWorld = config['KeyWorld']
    KeyWorld_Length = len(KeyWorld)
    app.run(debug=True, host='127.0.0.1', port=5701)  # 此处的 host和 port对应上面 yml文件的设置
