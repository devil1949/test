#!/usr/bin/env python3
# coding:utf-8

import threading
import time


def pro():
    print('dengren')
    event.wait()

    print('sb mai baozi')
    print('zuo baozi')
    time.sleep(3)
    event.set()


def con():
    print('maibaozi')
    event.set()

    time.sleep(2)
    print('dengdaimaibaozi')
    print(event.wait())


event = threading.Event()
