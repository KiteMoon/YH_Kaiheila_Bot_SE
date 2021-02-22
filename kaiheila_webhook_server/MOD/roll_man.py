#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 桜火, Inc. All Rights Reserved 
#
# @Time    : 2021/2/16 19:54
# @Author  : 桜火
# @Email   : xie@loli.fit
# @File    : roll_man.py
# @Software: PyCharm
import random


def roll(name, people_num):
	people_num = int(people_num / 2)  # 这里对传入人数进行判断，并且分配每边的人数
	print(people_num)
	if isinstance(name, list):  # 判断该变量是否为列表，如果是则执行程序，不是则弹出
		_success_a_list = []
		_success_b_list = []
		# 定义两个列表，用于存储列表人员数量
		while True:
			if name != []:
				if len(_success_a_list) < people_num:
					_a_team = (random.choice(name))
					name.remove(_a_team)
					_success_a_list.append(_a_team)

				else:
					_b_team = (random.choice(name))
					name.remove(_b_team)
					_success_b_list.append(_b_team)

			else:
				break
		_data = {
			"teamA": _success_a_list,
			"teamB": _success_b_list
		}
		return (_data)
	else:
		return ("error")


print(roll(["tom", "mary", "jack", "alice"], 4))
