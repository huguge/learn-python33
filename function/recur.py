#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# 利用递归函数计算阶乘
# N! = 1 * 2 * 3 * ... * N
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print('fact(1) =', fact(1))
print('fact(5) =', fact(5))
print('fact(10) =', fact(10))

# RecursionError: maximum recursion depth exceeded in comparison
# print('fact(1000) =', fact(1000))

# 利用递归函数移动汉诺塔
# 稍后需要理解
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
        return
    move(n-1, a, c, b)
    print('move', a, '-->', c)
    move(n-1, b, a, c)

# move(3, 'A', 'B', 'C')
move(4, 'A', 'B', 'C')
