#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
实现判断一个数是不是回文数的函数
"""
def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = temp % 10 + total * 10
        temp //= 10
    return total == num

x = int(input('请输入:'))
print(is_palindrome(x))