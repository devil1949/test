#!/usr/bin/env python3
# coding:utf-8

from threading import Thread
import time


class mythread(Thread):

    def run(self):
        Thread.run(self)


def Func(para):
    print(para)


t1 = mythread(target=Func, args=(1,))

t1.start()
print('over')
