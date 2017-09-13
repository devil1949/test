#！/usr/bin/env python3
# coding:utf-8

import socket
import requests


def handle_request(client):
    buf = client.recv(1024)
    print(buf)
    client.send(("HTTP/1.1 200 OK\r\n\r\n").encode())
    # client.send(("Content-Type:text/html\r\n\r\n").encode())
    client.send(("<a href='http://www.baidu.com'> hello, world </a>").encode())


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 7777))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()


if __name__ == '__main__':
    main()
