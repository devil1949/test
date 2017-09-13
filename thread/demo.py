#!/usr/bin/env python3
# coding:utf-8

from threading import Thread
from queue import Queue
import time


class Procuder(Thread):

    def __init__(self, name, queue):
        self.__Name = name
        self.__Queue = queue
        super(Procuder, self).__init__()

    def run(self):
        while True:
            if self.__Queue.full():
                time.sleep(1)
            else:
                self.__Queue.put('baozi')
                print('%s 生产了一个包子\n' % self.__Name)
                time.sleep(1)


class Consumer(Thread):

    def __init__(self, name, queue):
        self.__Name = name
        self.__Queue = queue
        super(Consumer, self).__init__()

    def run(self):
        while True:
            if self.__Queue.empty():
                time.sleep(1)
            else:
                self.__Queue.get()
                print('%s 消费了一个包子\n' % (self.__Name,))
                time.sleep(1)


que = Queue(maxsize=20)

for i in range(3):
    name = '厨师%d' % (i,)
    Procuder(name, que).start()

for i in range(10):
    name = '顾客%d' % (i,)
    Consumer(name, que).start()
