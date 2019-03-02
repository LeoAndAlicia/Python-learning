#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    def counter():
        return 1
    return counter
'''

def createCounter():
	L=[0]
	def counter():
		L[0] = L[0] + 1
		return L[0]
	return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')