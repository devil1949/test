#!/usr/bin/env python3
# coding:utf-8

import select
import socket
import sys
import queue


server = socket.socket()
server.setblocking(0)


server_address = ('127.0.0.1', 9999)
print('starting up on %s port %s' % server_address)
server.bind(server_address)


server.listen(5)


inputs = [server]
outputs = []
message_queue = {}

while inputs:
    print('\nwaiting for the next event')
    readable, writeable, exceptional = select.select(inputs, outputs, inputs)

    for s in readable:

        if s is server:

            connection, client_address = s.accept()
            print('new connection from', client_address)
            connection.setblocking(0)
            inputs.append(connection)

            message_queue[connection] = queue.Queue()

        else:
            data = s.recv(1024)
            if data:
                print('recevied "%s" from %s' % (data, s.getpeername()))
                message_queue[s].put(data)

                if s not in outputs:
                    outputs.append(s)
            else:
                print('closing', client_address)
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()

                del message_queue[s]

    for s in writeable:
        try:
            next_msg = message_queue[s].get_nowait()
        except queue.Empty:
            print('output queue for', s.getpeername(), 'is empty')
            outputs.remove(s)
        else:
            print('sending "%s" to %s' % (next_msg, s.getpeername()))
            s.send(next_msg)

    for s in exceptional:
        print('handling exceptional condition for', s.getpeername(), 'is error')
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()

        del message_queue[s]
