#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：

ax2 + bx + c = 0

的两个解。

提示：计算平方根可以调用math.sqrt()函数
import math

def quadratic(a, b, c):
'''
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
'''
print('二元一次方程ax^2+bx+c=0 求根公式\n')
a = int(input('请输入a = '))
b = int(input('请输入b = '))
c = int(input('请输入c = '))
print(quadratic(a,b,c))
'''

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')