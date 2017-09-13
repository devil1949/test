#!/usr/bin/env python3
# coding:utf-8

from multiprocessing import Pool
import time


def f(x):
    time.sleep(1)
    print(x)
    return x * x


if __name__ == '__main__':
    p = Pool(5)
    print(p.map(f, range(5)))
