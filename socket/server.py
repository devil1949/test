#！/usr/bin/env python3
# coding:utf-8

import socket

server = socket.socket()
ip_address = ('127.0.0.1', 9999)
server.bind(ip_address)
server.listen(5)


while True:
    conn, address = server.accept()
    conn.send(("hello").encode())

    while True:
        if conn.recv(1024) == "exit":
            break
        conn.sendall(bytes('ceshi', encoding="utf8"))
    conn.close()
