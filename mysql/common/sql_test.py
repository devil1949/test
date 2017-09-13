#!/usr/bin/env python3
# coding:utf-8

import pymysql


class sql_test(object):

    def __init__(self):
        pass

    def get_dict(self, sql, para):

        conn = pymysql.connect(host='127.0.0.1', port=3128,
                               user='root', passwd='aion', db='test', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        recount = cursor.execute(sql, para)
        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return data
