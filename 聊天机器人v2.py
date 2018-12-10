#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

while True:
    msg = input('\n我说：')
    reply = requests.post('http://api.itmojun.com/chat_robot', {'msg': msg}).text
    print('\n小智说：' + reply)