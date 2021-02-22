import json
import zlib

import sys, os
import sys

from MOD.route import *
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def wh_server(request):
	if (request.method == 'POST'):
		# print("检测到POST请求")
		postBody = request.body
		server_post_message = zlib.decompress(postBody).decode()
		server_post_message_disc = json.loads(server_post_message)
		if "challenge" in server_post_message_disc["d"]:
			_result_challenge = {
				"challenge": server_post_message_disc["d"]["challenge"]
			}
			print("服务器发送请求校对码")
			print(_result_challenge)
			return HttpResponse(json.dumps(_result_challenge))
		else:
			_push_data = {
				"sn": server_post_message_disc['sn']
			}
			# print((server_post_message_disc))整个消息块
			print("接收到非验证消息，消息序列为:" + str(server_post_message_disc['sn']))
			print("消息内容为")
			print(server_post_message_disc)
			ready_message_data(server_post_message_disc)
			return HttpResponse("json.dumps(_push_data)")

	else:
		print("接收到网页端GET请求，已经回执页面")
		return render(request, 'index.html')
