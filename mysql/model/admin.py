#!/usr/bin/env python3
# coding:utf-8

from common.sql_test import sql_test


class Admin(object):

    def __init__(self):
        self.__conn = sql_test()

    def get_one(self, id):
        sql = "selecet * from weddings where id=%s"
        para = (id,)
        return self.__conn.get_dict(sql, para)

    def check(self, p1, p2):
        sql = "select * from test where name=%s and pass=%s"
        para = (p1, p2,)
        return self.__conn.get_dict(sql, para)
