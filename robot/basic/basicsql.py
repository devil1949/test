#!/usr/bin/env python3
# coding:utf-8

import pymysql


class BasicSQL(object):

    def __init__(self):
        self.__connDict = {'host': '127.0.0.1', 'port': 3128,
                           'user': 'root', 'passwd': 'aion', 'db': 'test', 'charset': 'utf8'}

    def GetSimple(self, sql, para):
        conn = pymysql.connect(**self.__connDict)
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql, para)
        data = cur.fetchone()
        cur.close()
        conn.close()
        return data

    def GetDict(self, sql, para):
        conn = pymysql.connect(**self.__connDict)
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql, para)
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data

    def InsSample(self, sql, para):
        conn = pymysql.connect(**self.__connDict)
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        count = cur.execute(sql, para)
        conn.commit()
        cur.close()
        conn.close()
        return count

    def InsSample_ReturnId(self, sql, para):
        conn = pymysql.connect(**self.__connDict)
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql, para)
        id = cur.lastrowid
        conn.commit()
        cur.close()
        conn.close()
        return id
