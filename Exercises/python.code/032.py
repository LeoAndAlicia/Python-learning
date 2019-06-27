#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
寻找“完美数”
"""
import math
def main():
	for num in range(1,10000):
		sum = 0
		for factor in range(1, int(math.sqrt(num))+1):
			if num % factor == 0:
				sum += factor
				if (factor > 1) and (num / factor != factor):
					sum += num / factor
		if num != 1 and sum == num:
			print(num)

if __name__ == "__main__":
	main()