#!/usr/bin/env python3
# coding:utf-8

import redis


class BasicRedis(object):

    def __init__(self):
        self.__conn = redis.Redis(host='127.0.0.1')

        self.chan_sub = 'fm87.7'
        self.chan_pub = 'fm104.5'

    def get(self, key):
        return self.__conn.get(key)

    def set(self, key, value):
        self.__conn.set(key, value)

    def public(self, msg):
        self.__conn.publish(self.chan_pub, msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub
