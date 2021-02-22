#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 桜火, Inc. All Rights Reserved 
#
# @Time    : 2021/2/16 20:46
# @Author  : 桜火
# @Email   : xie@loli.fit
# @File    : route.py
# @Software: PyCharm
import re

from MOD.bilibili_video import _result_bilibili_video_info
from MOD.rainbow_six import get_r6_Foundation_info


def ready_message_data(message_data):
    # print("-----对比-----")
    # print(message_data)
    print(type(message_data))
    print(message_data['d']["channel_type"])
    print((message_data))
    print("聊天室ID:" + str(message_data['d']["channel_type"]))
    route_admin(message_data['d'])
    return message_data['d']


def route_admin(json_all_data):
    message_room_id = json_all_data['target_id']
    message_text = json_all_data['content']
    if re.match("/rool", message_text):
        print("进入roll人视图")
    elif re.match("/stop roll", message_text):
        print("roll人完毕")
    elif re.match("/BV", message_text):
        print("进入bilibili查询视图")
        _BVID = (re.sub("/BV", "", message_text, flags=1)).strip()

        print(_result_bilibili_video_info(_BVID, message_room_id))
    elif re.match("/R6", message_text):
        print("进入R6查询视图")
        _name = (re.sub("/R6", "", message_text, flags=1)).strip()
        get_r6_Foundation_info(_name, message_room_id)
    else:
        print("hello")
