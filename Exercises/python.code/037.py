#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
实现判断一个数是不是素数的函数
"""
def is_prime(num):
    if num > 1:
        for factor in range(2, num):
            if num % factor == 0:
                return False
        return True
    else:
        return False

x = int(input('请输入:'))
print(is_prime(x))