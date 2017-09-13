#!/usr/bin/env python3
# coding:utf-8

import threading
import time

num = 0


def run(n):
    global num
    time.sleep(0.1)

    lock.acquire()
    num += 1
    lock.release()

    print(num)


lock = threading.RLock()
#lock = threading.BoundedSemaphore(1)

for i in range(10):
    threading.Thread(target=run, args=(i,)).start()
