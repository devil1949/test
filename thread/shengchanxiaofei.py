#!/usr/bin/env python3
# coding:utf-8

import time
import random
import queue
import threading


def Proudcer(name, que):
    while True:
        if que.qsize() < 3:
            que.put('baozi')
            print('%s 生产了一个包子==============' % (name))
        else:
            print('还有3个包子。。。')
        time.sleep(random.randrange(3))


def Consumer(name, que):
    while True:
        try:
            que.get_nowait()
            print('%s 消费了一个包子' % (name))
        except Exception:
            print('没有包子了。。。')
        time.sleep(random.randrange(3))


q = queue.Queue()

for i in range(2):
    name = '厨师%d' % (i,)
    threading.Thread(target=Proudcer, args=(name, q,)).start()

for i in range(4):
    name = '顾客%d' % (i,)
    threading.Thread(target=Consumer, args=(name, q,)).start()
