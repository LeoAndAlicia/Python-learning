#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复：
'''

from functools import reduce

def str2num(s):
	if '.' in s:
		return float(s)
	else :
		return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()




# 测试:


http://of66as8gb.bkt.clouddn.com/12.2%20xss%E6%94%BB%E5%87%BB%E5%8E%9F%E7%90%86%E5%8F%8A%E9%98%B2%E8%8C%83.mp4




