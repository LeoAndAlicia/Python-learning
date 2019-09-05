#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
设计一个函数返回给定文件名的后缀名
"""
def get_suffix(filename, has_dot = False):
    """
    :param filename: 文件名
    :param has_dot: 后缀名是否需要带点
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot == True else pos + 1
        print(filename[index:])
    else:
        print('')

if __name__ == '__main__':
    get_suffix('abc.exe', True)