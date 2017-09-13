#！/usr/bin/env python3
# coding:utf-8

from wsgiref.simple_server import make_server


def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    httpd = make_server('', 9999, RunServer)
    print('Serving HTTP on port 9999....')
    httpd.serve_forever()
