#！/usr/bin/env python3
# coding:utf-8

from basic.basicsql import BasicSQL


class UserInfo(object):

    def __init__(self):
        self.basicsql = BasicSQL()

    def CheckLogin(self, name, pwd):
        sql = 'select id,name,pass from userinfo where name=%s and pass=%s'
        para = (name, pwd,)
        result = self.basicsql.GetSimple(sql, para)

        if not result:
            return False
        else:
            return result['id']


class ChatRecord(object):

    def __init__(self):
        self.basicsql = BasicSQL()

    def InsertRecord(self, message, date, userid):
        sql = 'insert into chatrecord (message,date,userid) values(%s,%s,%s)'
        para = (message, date, userid)
        result = self.basicsql.InsSample(sql, para)

    def GetRecord(self, userid):
        sql = 'select message,date,userid from chatrecord where userid=%s'
        para = (userid,)
        return self.basicsql.GetDict(sql, para)
