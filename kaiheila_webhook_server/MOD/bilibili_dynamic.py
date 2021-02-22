#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 桜火, Inc. All Rights Reserved 
#
# @Time    : 2021/2/19 16:21
# @Author  : 桜火
# @Email   : xie@loli.fit
# @File    : bilibili_dynamic.py
# @Software: PyCharm
import requests
import pymysql
import json


def get_bilibili_dynamic(UID):
	print("进入方法的UID为:" + str(UID))
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.47 Safari/537.36 Edg/89.0.774.27",
		"Origin": "https://space.bilibili.com",
		"Sec-Fetch-Site": "same-site",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Dest": "empty",
		"Referer": "https://space.bilibili.com/",
		"Cookie": "l=v; _uuid=030CF8B2-4699-D6F2-7D78-9F802EC997E562133infoc; buvid3=0BFE615D-9523-4B4E-90B4-94E385671EEE143094infoc; sid=jpvmhspz; DedeUserID=37958451; DedeUserID__ckMd5=58b01ed465ac1c5e; SESSDATA=79a3e1a3%2C1622035472%2C34146*b1; bili_jct=487a0cf4b755075012ddfb5adbf0e63d; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(um)~uml)kY0J'uY|YR)JR)u; LIVE_BUVID=AUTO6916064885389528; buvid_fp_plain=0BFE615D-9523-4B4E-90B4-94E385671EEE143094infoc; buivd_fp=0BFE615D-9523-4B4E-90B4-94E385671EEE143094infoc; CURRENT_QUALITY=116; buvid_fp=0BFE615D-9523-4B4E-90B4-94E385671EEE143094infoc; balh_server_inner=__custom__; balh_is_closed=; bp_video_offset_37958451=484944087382561530; fingerprint3=e6a79e5e514e6988ff273238610536dc; fingerprint=dfc25dcb3c20694387f77bf16d4c3824; fingerprint_s=f6eeafeb2ff34f0a6e507e3c04aa4521; PVID=3; bp_t_offset_37958451=493414669132174862"
	}
	_dynamic_url = "https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history?visitor_uid=" + str(UID) + \
	               "&host_uid=" + str(UID) + "&offset_dynamic_id=0&need_top=1&platform=web"

	try:
		bilibili_dynamic_get = requests.get(url=_dynamic_url, headers=headers)
		bilibili_dynamic_get.status_code
	except:
		error_text = "发生错误，错误地点BILIBILI_DYNMIC 33"
		print(error_text)
	else:
		bilibili_dynamic_get_json = bilibili_dynamic_get.json()
		bilibili_dynamic_result_all = bilibili_dynamic_get_json["data"]["cards"][1]["card"]  # 列表第一个索引是用户名，第二个是动态
		print(bilibili_dynamic_get_json)
		print(bilibili_dynamic_result_all)
		ccc = json.loads(bilibili_dynamic_result_all)
		print(bilibili_dynamic_get_json)
		print(ccc)
		print(ccc["user"]["name"])  # 转发人的名称
		print(ccc["item"]["description"])  # 转发人转发动态的蚊子
		print(bilibili_dynamic_result_all)
		aaa = json.loads(ccc["origin"])
		print(aaa["item"]["description"])  # 转发的动态主体文字
		img_num = (len(aaa["item"]["pictures"]))
		img = (aaa["item"]["pictures"])
		for num in range(0, (img_num)):
			print(img[num]["img_src"])
			print(num)
