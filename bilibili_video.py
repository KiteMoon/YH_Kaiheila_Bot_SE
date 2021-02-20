#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 桜火, Inc. All Rights Reserved 
#
# @Time    : 2021/2/17 13:39
# @Author  : 桜火
# @Email   : xie@loli.fit
# @File    : bilibili_video.py
# @Software: PyCharm
import requests
import time
from kaiheila_post_card_message import post_kaiheila_message
from data_process import timestamp

headers = {

    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.47 Safari/537.36 Edg/89.0.774.27",
    "Accept": "*/*",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.bilibili.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
}


def get_video_player(aid):
    print(aid)
    _url_aid = "http://api.bilibili.com/archive_stat/stat?aid=" + str(aid) + "&type=jsonp"
    _video_player = requests.get(url=_url_aid, headers=headers)
    _video_player_json = _video_player.json()
    return _video_player_json


def get_video_info(bvid):
    print(bvid)
    _url_bid = "https://api.bilibili.com/x/web-interface/view?bvid=" + bvid
    _video_info = requests.get(url=_url_bid, headers=headers)
    _video_info_json = _video_info.json()
    return _video_info_json


def time_list(time_num):
    time_data = time.localtime(time_num)


def _result_bilibili_video_info(bvid, target_id):
    _url_test_bid = "https://api.bilibili.com/x/web-interface/view?bvid=" + bvid
    _video_test_info = requests.get(url=_url_test_bid, headers=headers)
    _video_test_info_json = _video_test_info.json()
    print(_video_test_info_json)
    if _video_test_info_json["code"] == 0:

        _video_info_json = get_video_info(bvid)
        _video_info_player = get_video_player(_video_info_json["data"]["aid"])
        _result_disc = {
            "title": _video_info_json["data"]["title"],
            "pic": _video_info_json["data"]["pic"],
            "author": _video_info_json["data"]["owner"]["name"],
            "author_id": _video_info_json["data"]["owner"]["mid"],
            "aid": _video_info_json["data"]["aid"],
            "desc": _video_info_json["data"]["desc"],
            "time": timestamp(_video_info_json["data"]["ctime"]),
        }
        content = "视频名称：" + _video_info_json["data"]["title"] + "\n视频作者：" + _video_info_json["data"]["owner"]["name"] \
                  + "\n分区：" + _video_info_json["data"]["tname"] + "\n视频AV号：" + str(
            _video_info_json["data"]["aid"]) + "\n视频发布时间：" \
                  + str(timestamp(_video_info_json["data"]["ctime"])) + "\n视频播放量：" + str(
            _video_info_json["data"]["stat"]["view"]) \
                  + "\n视频点赞量：" + str(_video_info_json["data"]["stat"]["like"]) + "\n视频硬币数：" + str(
            _video_info_json["data"]["stat"]["coin"]) \
                  + "\n视频分享量：" + str(_video_info_json["data"]["stat"]["share"]) + "\n视频收藏量：" + str(
            _video_info_json["data"]["stat"]["favorite"]) \
                  + "\n视频弹幕数：" + str(_video_info_json["data"]["stat"]["danmaku"])
        card_view = [
            {
                "type": "card",
                "theme": "secondary",
                "size": "lg",
                "modules": [
                    {
                        "type": "section",
                        "text": {
                            "type": "plain-text",
                            "content": content
                        },
                        "mode": "right",
                        "accessory": {
                            "type": "image",
                            "src": _video_info_json["data"]["pic"],
                            "size": "lg"
                        }
                    },
                    {
                        "type": "action-group",
                        "elements": [
                            {
                                "type": "button",
                                "theme": "primary",
                                "value": "https://www.bilibili.com/video/av" + str(_video_info_json["data"]["aid"]),
                                "click": "link",
                                "text": {
                                    "type": "plain-text",
                                    "content": "前往视频地址"
                                }
                            },
                            {
                                "type": "button",
                                "theme": "danger",
                                "value": _video_info_json["data"]["pic"],
                                "click": "link",
                                "text": {
                                    "type": "plain-text",
                                    "content": "获取封面"
                                }
                            }
                        ]
                    }
                ]
            }
        ]
        _post_message_url = "https://www.kaiheila.cn/api/v3/channel/message"
        message_data = {
            "type": "10",
            "channel_id": str(target_id),
            "content": card_view
        }
        post_kaiheila_message("10", target_id, card_view)
    else:

        return ("error")
