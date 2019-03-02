#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
from functools import reduce

def str2float(s):
	pass
'''

from functools import reduce
def str2float(s):
	n = s.index('.')
	a = list(map(int ,[x for x in s[:n]]))
	b = list(map(int ,[x for x in s[n+1:]]))
	return reduce(lambda x,y: 10*x+y, a) + reduce(lambda x,y: 10*x+y, b)/10**len(b)


# 测试:
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')