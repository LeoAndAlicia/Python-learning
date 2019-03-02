#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    pass
'''

def normalize(name):
	return name.capitalize()



# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
if L2 == ['Adam', 'Lisa', 'Bart']:
	print('测试成功！')
else:
	print('测试失败！')