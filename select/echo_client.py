#!/usr/bin/env python3
# coding:utf-8

import socket
import sys
import time

server_address = ('localhost', 9999)
messages = ['This is the message. ', 'It will be sent ', 'in parts.']
socks = [socket.socket(), socket.socket()]

print('connecting to %s port %s' % server_address)
for s in socks:
    s.connect(server_address)

for message in messages:
    for s in socks:
        print('%s: sending "%s"' % (s.getsockname(), message))
        s.send(message.encode())
        time.sleep(1)

    for s in socks:
        data = s.recv(1024)
        print('%s: received "%s"' % (s.getsockname(), data))
        if not data:
            print('closing socket', s.getsockname())
