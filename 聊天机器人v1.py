#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: dj
@contact: dj@itmojun.com
@software: PyCharm
@file: main.py
@time: 2018/10/26 11:00
"""

import json
from urllib import request, parse

def get_robot_reply(input_text):
    data = {
        "reqType":0,
        "perception": {
            "inputText": {
                "text": input_text
            },
        },
        "userInfo": {
            "apiKey": "cc8c863cfa2b42ecb1e6ae9d4f2c5f36",
            "userId": "339745"
        }
    }
    data = json.dumps(data, ensure_ascii=False).encode("utf-8")
    # data = parse.urlencode(data).encode("utf-8")
    # print(data)
    url = request.Request("http://openapi.tuling123.com/openapi/api/v2", data=data, method="POST")
    res = request.urlopen(url).read()

    return json.loads(res.decode("utf-8"))["results"][0]["values"]["text"]


def main():
    while(True):
        input_text = input("\n我说：")
        print("\n小魔仙说：", get_robot_reply(input_text), sep="")

if __name__ == '__main__':
    main()
