#!/usr/bin/env python3
# coding:utf-8

import socket
import sys
import json

sk = socket.socket()
sk.connect(('127.0.0.1', 9999))

while True:
    data = sk.recv(2048)
    rev_data = json.loads(data)
    print(rev_data['data'])

    if not rev_data['key']:
        user = input('username:')
        pwd = input('password:')
        rev_data['data'] = [user, pwd]
        sk.sendall(json.dumps(rev_data).encode())
    else:
        inp = input('reply:')
        rev_data['data'] = inp
        sk.sendall(json.dumps(rev_data).encode())
        if inp == 'exit':
            print('88')
            exit()
