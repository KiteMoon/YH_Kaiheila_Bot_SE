#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 桜火, Inc. All Rights Reserved 
#
# @Time    : 2021/2/19 17:00
# @Author  : 桜火
# @Email   : xie@loli.fit
# @File    : bilibili_dynamic_listener.py
# @Software: PyCharm
import pymysql
import time
import configparser
import os
from bilibili_dynamic import get_bilibili_dynamic

config_info = configparser.ConfigParser()
fui = config_info.read("config.ini")
mysql_info_host = config_info.get("mysql", "host")
mysql_info_name = config_info.get("mysql", "db_name")
mysql_info_username = config_info.get("mysql", "username")
mysql_info_password = config_info.get("mysql", "password")
sql = "SELECT UID FROM bilibili_dynamic"
_result_list = []
while True:
	db = pymysql.connect(host=mysql_info_host, user=mysql_info_username, password=mysql_info_password,
	                     database=mysql_info_name)
	_result_list = []
	cursor = db.cursor()
	cursor.execute(sql)
	results = cursor.fetchall()
	for _result in results:
		for _result_num in _result:
			print(_result_num)
			get_bilibili_dynamic(_result_num)

	time.sleep(10)
