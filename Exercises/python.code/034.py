#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成斐波那契数列
"""
def fibo(num):
    numlist = [0 ,1]
    for x in range(num - 2):
        numlist.append(numlist[-2] + numlist[-1])
    print(numlist)

if __name__ == "__main__":
    fibo(10)