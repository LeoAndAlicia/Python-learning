"""
输入半径计算圆的周长和面积
"""
import math

radius = float(input('请输入圆的半径:'))
perimeter = 2 * radius * math.pi
area = math.pi * radius * radius
print('周长=%.1f,面积=%.1f' % (perimeter,area))