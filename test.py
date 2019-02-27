#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def quadratic(a,b,c):
    if a == 0:
        raise TypeError('a不能为0')
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)) or not isinstance(c,(int,float)):
        raise TypeError('Bad operand type')
    s = b**2 - 4*a*c
    if s < 0:
        return '无实根'
    if s == 0:
    	x1= (-b+math.sqrt(s))/2/a
    	return x1
    else:
        x1= (-b+math.sqrt(s))/2/a
        x2= (-b-math.sqrt(s))/2/a
        return x1,x2
print('二元一次方程ax^2+bx+c=0 求根公式\n')
a = int(input('请输入a = '))
b = int(input('请输入b = '))
c = int(input('请输入c = '))

print(quadratic(a,b,c))
