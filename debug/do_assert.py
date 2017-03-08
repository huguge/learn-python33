#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def foo(s):
    n = int(s) # 将s转换成int类型
    # 断言进行中
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

main()