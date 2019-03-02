#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
请用匿名函数改造下面的代码：
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
print(L)
'''

L = list(filter(lambda n:n % 2 == 1,range(1,20)))
print(L)


# 测试: