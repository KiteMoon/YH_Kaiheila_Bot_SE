#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 桜火, Inc. All Rights Reserved 
#
# @Time    : 2021/2/16 21:13
# @Author  : 桜火
# @Email   : xie@loli.fit
# @File    : shaizi.py
# @Software: PyCharm
import asyncio
import websockets
import json
import zlib
import requests
import random
from route import route_admin
from roll_man import roll

headers = {
	"Authorization": "Bot 1/MTAxNjA=/ugnbLazYqwKY8+wFl+65gA==",
	"compress": "0"
}


def get_ws():
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
			if json_all_data["type"] == 1:
				json_all_data_text = json_all["d"]["content"]
				if json_all_data_text == "/roll":
					data = {
						"type": "1",
						"channel_id": json_all["d"]["target_id"],
						"content": str(random.randint(1, 6))
					}
					requests.post("https://www.kaiheila.cn/api/v3/channel/message", headers=headers, data=data)


if __name__ == "__main__":
	asyncio.get_event_loop().run_until_complete(send_hello())
