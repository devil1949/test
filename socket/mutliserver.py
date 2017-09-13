#！/usr/bin/env python3
# coding:utf-8

import socketserver


class myserver(socketserver.BaseRequestHandler):

    def setup(self):
        pass

    def handle(self):
        conn = self.request
        conn.send(('hello').encode())
        while True:
            if conn.recv(1024) == "exit":
                break
            conn.send(('ceshi').encode())
        conn.close()

    def finish(self):
        pass


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), myserver)
    server.serve_forever()
