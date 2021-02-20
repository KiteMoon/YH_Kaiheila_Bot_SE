#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 桜火, Inc. All Rights Reserved 
#
# @Time    : 2021/2/16 10:21
# @Author  : 桜火
# @Email   : xie@loli.fit
# @File    : client.py.py
# @Software: PyCharm
import threading
import asyncio
import websockets
import json
import zlib
import requests
from test import *
from route import route_admin
from roll_man import roll


def get_ws():
    headers = {
        "Authorization": "Bot 1/MTAxNjA=/ugnbLazYqwKY8+wFl+65gA==",
        "compress": "0"
    }
    ws_url = requests.get("https://www.kaiheila.cn/api/v3/gateway/index", headers=headers).json()
    if (ws_url["code"]) == 0:
        print(ws_url["data"]["url"])
        return (ws_url["data"]["url"])
    else:
        print("错误")
        return ("error")


url = ""


async def send_hello():
    if get_ws() == "error":
        print("发生异常")
    else:
        url = get_ws()
    async  with websockets.connect(url) as websocket:

        while True:
            greeting = await websocket.recv()
            greetings = zlib.decompress(greeting).decode()
            print(greetings)

            json_all = json.loads(greetings)
            json_all_scode = json_all["s"]
            json_all_data = json_all["d"]
            if json_all_scode == 1:
                continue
            ws_scode = json_all["sn"]
            print("当前消息序列：" + str(ws_scode))
            if json_all_data["type"] == 1:
                route_admin(json_all_data)
                send_target_id = (json_all_data['target_id'])
                send_people_id = (json_all_data['author_id'])
                send_data = (json_all_data['content'])
                print("ID:" + str(send_people_id) + "\n在频道ID：" + str(send_target_id) + "\n发送消息：" + send_data)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(send_hello())
