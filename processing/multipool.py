#!/usr/bin/env python3
# coding:utf-8

from multiprocessing import Pool
import time


def f(x):
    print(x * x)
    time.sleep(1)
    return x * x


pool = Pool(processes=4)
res_list = []

for i in range(10):
    res = pool.apply_async(f, [i, ])
    print('----:%s' % i)
    res_list.append(res)

#for r in res_list:
#    print(r.get())


#print(pool.map(f, range(10,)))
