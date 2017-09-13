#!/usr/bin/env python3
# coding:utf-8

from model.admin import Admin


def main():
    user = input('username:')
    pwd = input('password:')

    admin = Admin()
    result = admin.check(user, pwd)

    print(result)

    if not result:
        print('mimacuowu!')
    else:
        print('dengluchenggong!')


if __name__ == '__main__':
    main()
