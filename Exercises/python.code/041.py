#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
设计一个函数返回传入的列表中最大和第二大的元素的值
"""
def max2(x):
    m1 ,m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        else:
            m2 = x[index]
    print(m1, m2)

if __name__ == '__main__':
    max2([1,2,3,4,5,7])