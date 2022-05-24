import time
from plugins.send_msg import *
def dinshixiaoxi(temp,config,messages):
    print(time.time())
    if temp["LaunchNotification"] == "false":
        send_msg('private',config["owner"],messages["机器人_启动"])
        temp["LaunchNotification"] = "true" 