#!/usr/bin/env python
# coding=utf-8

'''
求100!各位相加之和
'''

n = 1
for i in range(1, 101):
    n *= i
num = len(str(n))
print n, num
ans = 0
for i in range(1, num + 1):
    tmp1 = 10 ** (num - i)
    tmp2 = n / tmp1
    ans += tmp2 
    n %= tmp1
print ans
