#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
'''

import functools
def log(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        print('begin call %s' % fn.__name__)
        result = fn(*args,**kw)
        print('end call %s' % fn.__name__)
        return result
    return wrapper

# 测试:
@log
def now():
    print('now')

now()