#!/usr/bin/env python3
# coding:utf-8

from multiprocessing import Process
import os


def info(title):
    print(title)
    print('module name:', __name__)
    if hasattr(os, 'getppid'):
        print('parent process:', os.getppid())
    print('print id:', os.getpid())


def f(name):
    info('func f')
    print('hello', name)


if __name__ == '__main__':
    info('main line')
    print('-----------------')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
