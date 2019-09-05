#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
实现计算求最大公约数和最小公倍数的函数
"""
def gcd(x, y):
    if x > y:
        x , y = y, x
    for factor in range(x , 0 , -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    return x * y // gcd(x, y)