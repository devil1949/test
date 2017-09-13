#!/usr/bin/env python3
# coding:utf-8

from multiprocessing import Process, Manager, Queue, Values, Array


def f(d, l):
    d[l] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()


if __name__ == '__main__':
    manager = Manager()

    d = manager.dict()
    l = manager.list(range(10))

    p = Process(target=f, args=(d, l))
    p.start()
    p.join()

    print(d)
    print(l)
