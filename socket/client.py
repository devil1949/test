#！/usr/bin/env python3
# coding:utf-8

import socket

client = socket.socket()
ip_address = ('127.0.0.1', 9999)
client.connect(ip_address)

while True:
    data = client.recv(1024)
    print(data)
    shuju = input()
    client.sendall(bytes(shuju, encoding="utf8"))
    if shuju == "exit":
        break
