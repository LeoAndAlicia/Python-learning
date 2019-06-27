#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
百钱百鸡
"""
for x in range(0,20):
	for y in range(0,33):
		z=100-x-y
		if 5*x+3*y+z/3 == 100 and x != 0 and y != 0 and z != 0:
			print(x, y , z)