#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# print('L[0:3] = ', L[0:3])
# print('L[:3] = ', L[:3])
# print('L[1:3] = ', L[1:3])
# print('L[-2:] = ', L[-2:])

R = list(range(100))
# 取前10个数
print('R[:10] = ', R[:10])
# 取倒数10个数
print('R[-10:] = ', R[-10:])
# 取 10-20的数，不包括20
print('R[10:20] = ', R[10:20])
# 前10个数，每2个去一个
print('R[:10:2] = ', R[:10:2])
# 所有的数，每5个取一个
print('R[::5] = ', R[::5])
# 什么都不写，只写[:] 就可以原样复制一个list
print('L[:] = ', L[:])
# tuple 也是一个list，唯一区别是tuple不可变
# 因此tuple也可以用切片操作，只是结果仍为tuple
print((0,1,2,3,4,5)[:3])
# 字符串‘xxx’ 也可以看成是一个list，结果仍为字符串
print('ABCDEFG'[:3])
# 每2个取一个值
print('ABCDEFG'[::2])

# print([L[0], L[1], L[2]])

r = []
n = 3
for i in range(n):
    r.append(L[i])
# print('r = ', r)


