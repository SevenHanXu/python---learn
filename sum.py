#!/usr/bin/env python
# coding=utf-8

'''
输入n个数字，输出n个数字之和
'''

n = int(raw_input("Please input n : "))
sum = 0
for i in range(1, n + 1):
    num = int(raw_input("Please input %d's num :  " % i))
    sum += num
print sum
