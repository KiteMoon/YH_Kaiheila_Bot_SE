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
from roll_man import roll
from rainbow_six import get_r6_Foundation_info
from bilibili_video import _result_bilibili_video_info
import re


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
