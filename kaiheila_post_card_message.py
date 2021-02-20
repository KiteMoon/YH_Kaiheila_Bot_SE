#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 桜火, Inc. All Rights Reserved 
#
# @Time    : 2021/2/19 22:57
# @Author  : 桜火
# @Email   : xie@loli.fit
# @File    : kaiheila_post_card_message.py
# @Software: PyCharm
import requests
import configparser
import os
import json

config_info = configparser.ConfigParser()
fui = config_info.read("config.ini")
Authorization = config_info.get("kaiheila", "websockt_token")


def post_kaiheila_message(message_class, channel_id, message_data):
    card_message_data = {
        "type": str(message_class),
        "channel_id": str(channel_id),
        "content": json.dumps(message_data)
    }
    _post_message_url = "https://www.kaiheila.cn/api/v3/channel/message"
    _post_kaiheila_message_requests = requests.post(url=_post_message_url, headers={"Authorization": Authorization},
                                                    data=card_message_data)
    print(card_message_data)
    print(_post_kaiheila_message_requests.text)
