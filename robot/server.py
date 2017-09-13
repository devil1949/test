#！/usr/bin/env python3
# coding:utf-8

import socketserver
import json
import time
from basic.models import UserInfo, ChatRecord


class myserver(socketserver.BaseRequestHandler):

    def setup(self):
        pass

    def handle(self):
        userinfo = UserInfo()
        chatrecord = ChatRecord()

        container = {'key': '', 'data': ''}
        container['data'] = 'ok...'

        conn = self.request
        conn.sendall(json.dumps(container).encode())

        Flag = True
        while Flag:
            try:
                data = conn.recv(2048)
                rev_data = json.loads(data)

                if rev_data['data'] == 'exit':
                    conn.close()
                    break

                if not rev_data['key']:
                    name, pwd = rev_data['data']
                    re = userinfo.CheckLogin(name, pwd)
                    if re:
                        rev_data['key'] = re
                        rev_data['data'] = 'yuema'
                    else:
                        rev_data['data'] = 'failed'
                    conn.sendall(json.dumps(rev_data).encode())
                else:
                    datetime = time.strftime('%Y-%m-%d %H:%M:%S')

                    if rev_data['data'] == 'list':
                        rev_data['data'] = chatrecord.GetRecord(
                            rev_data['key'])
                        print(rev_data['data'])

                    elif rev_data['data'].__contains__('yes'):
                        chatrecord.InsertRecord(
                            rev_data['data'], datetime, rev_data['key'])
                        rev_data['data'] = 'I am a hero'
                        chatrecord.InsertRecord(
                            rev_data['data'], datetime, rev_data['key'])

                    else:
                        chatrecord.InsertRecord(
                            rev_data['data'], datetime, rev_data['key'])
                        rev_data['data'] = 'what?'
                        chatrecord.InsertRecord(
                            rev_data['data'], datetime, rev_data['key'])
                    conn.sendall(json.dumps(rev_data).encode())
            except Exception as e:
                print(e)
                Flag = False

    def finish(self):
        pass


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), myserver)
    server.serve_forever()
