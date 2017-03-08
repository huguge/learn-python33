#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {'a':1, 'b':2, 'c':3}
for key in d:
    # dic不是顺序排列的，打印出来的顺序可能不一样
    print(key)

for ch in 'ABC':
    print(ch)

from collections import Iterable
# str 是否可迭代
print('isinstance(\'abc\', Iterable)', isinstance('abc', Iterable))
# list是否可迭代
print('isinstance([1,2,3], Iterable)', isinstance([1,2,3], Iterable))
# 整数是否可迭代
print('isinstance(123, Iterable)', isinstance(123, Iterable))
