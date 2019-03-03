#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
再思考一下能否写出一个@log的decorator，使它既支持：

@log
def f():
    pass
又支持：

@log('execute')
def f():
    pass
'''

import functools
def log(text):
	def decorator(fn):
		@functools.wraps(fn)
		def wrapper(*args,**kw):
			if isinstance(text,(int,str)):
				print('%s call %s' % (text,fn.__name__))
			else :
				print('call %s' % fn.__name__)
			return fn(*args,**kw)
		return wrapper
	return decorator if isinstance(text,(int,str)) else decorator(text)


# 测试:
@log
def a():
	print('a')

@log('b')
def b():
	print('b')

@log('c')
def c():
	print('c')

a()
b()
c()