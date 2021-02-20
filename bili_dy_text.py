import requests
import json
from kaiheila_post_card_message import post_kaiheila_message

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.47 Safari/537.36 Edg/89.0.774.27",
	"Origin": "https://space.bilibili.com",
	"Sec-Fetch-Site": "same-site",
	"Sec-Fetch-Mode": "cors",
	"Sec-Fetch-Dest": "empty",
	"Referer": "https://space.bilibili.com/",
	"Cookie": "l=v; _uuid=030CF8B2-4699-D6F2-7D78-9F802EC997E562133infoc; buvid3=0BFE615D-9523-4B4E-90B4-94E385671EEE143094infoc; sid=jpvmhspz; DedeUserID=37958451; DedeUserID__ckMd5=58b01ed465ac1c5e; SESSDATA=79a3e1a3%2C1622035472%2C34146*b1; bili_jct=487a0cf4b755075012ddfb5adbf0e63d; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(um)~uml)kY0J'uY|YR)JR)u; LIVE_BUVID=AUTO6916064885389528; buvid_fp_plain=0BFE615D-9523-4B4E-90B4-94E385671EEE143094infoc; buivd_fp=0BFE615D-9523-4B4E-90B4-94E385671EEE143094infoc; CURRENT_QUALITY=116; buvid_fp=0BFE615D-9523-4B4E-90B4-94E385671EEE143094infoc; balh_server_inner=__custom__; balh_is_closed=; bp_video_offset_37958451=484944087382561530; fingerprint3=e6a79e5e514e6988ff273238610536dc; fingerprint=dfc25dcb3c20694387f77bf16d4c3824; fingerprint_s=f6eeafeb2ff34f0a6e507e3c04aa4521; PVID=3; bp_t_offset_37958451=493414669132174862"
}
UID = 37958451
_dynamic_url = "https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history?visitor_uid=" + str(UID) + \
               "&host_uid=" + str(UID) + "&offset_dynamic_id=0&need_top=1&platform=web"
bilibili_dynamic_get = requests.get(url=_dynamic_url, headers=headers)
bilibili_dynamic_get.status_code
bilibili_dynamic_get_json = bilibili_dynamic_get.json()
bilibili_dynamic_result_all = bilibili_dynamic_get_json["data"]["cards"][1]["card"]  # 列表第一个索引是用户名，第二个是动态
print(bilibili_dynamic_get_json)
print(bilibili_dynamic_result_all)
ccc = json.loads(bilibili_dynamic_result_all)
print(bilibili_dynamic_get_json)
print(ccc)
print(ccc["user"]["uname"])  # 转发人的名称
print(ccc["item"]["content"])  # 转发人转发动态的蚊子
print(bilibili_dynamic_result_all)
aaa = json.loads(ccc["origin"])
print(aaa["item"]["description"])  # 转发的动态主体文字
img_num = (len(aaa["item"]["pictures"]))
img = (aaa["item"]["pictures"])
elements = []
for num in range(0, (img_num)):
	_img_url = ""
	_img_url = (img[num]["img_src"]) + "@320w_267h_1e_1c.jpg"
	_tests = {
		"type": "image",
		"src": _img_url
	}
	elements.append(_tests)
content = "**昵称**：" + (ccc["user"]["uname"]) + "\n**动态内容**：\n" + (ccc["item"]["content"]) + (aaa["item"]["description"])
print("----------------")
print(content)
card_message = [
	{
		"type": "card",
		"theme": "secondary",
		"size": "lg",
		"modules": [
			{
				"type": "section",
				"text": {
					"type": "kmarkdown",
					"content": (content)
				}
			},
			{
				"type": "image-group",
				"elements": elements
			}
		]
	}
]
card_message_data = {
	"type": "10",
	"channel_id": str(6527406177738126),
	"content": json.dumps(card_message)
}
print(card_message)
card_message_json = json.dumps(card_message_data)
print(card_message_json)

post_kaiheila_message("10", 6527406177738126, card_message)
