#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
寻找“水仙花数”。
"""
for x in range(100,1000):
    a = int(str(x)[0])
    b = int(str(x)[1])
    c = int(str(x)[2])
    if x == (a ** 3 + b ** 3 +c ** 3):
        print(x)
