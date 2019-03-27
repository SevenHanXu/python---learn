#!/usr/bin/env python
# coding=utf-8

a = 10
b = 4
print ("%d + %d = ") % (a, b), a + b
print ("%d - %d = ") % (a, b), a - b
print ("%d * %d = ") % (a, b), a * b
print ("%d * 1.0 / %d = ") % (a, b), a * 1.0 / b
print ("%d * 1.0 // %d = ") % (a, b), a * 1.0 // b
print ("%d / %d = ") % (a, b), a / b
print ("%d // %d = ") % (a, b), a // b

c = int(raw_input("c = "))
d = int(raw_input("d = "))
print "%d + %d = " % (c, d) , c + d
print "%f + %f = " % (c, d) , c + d

e = 1
for i in range(1, 100):
    e *= i
print e
print range(1, 100)

f = "Hello "
g = "World !!!"
print f + "hanxu"
print f * 2 + g

h = '''
这是一行注释
韩旭是个美丽的女人
温柔可爱又大方
'''
print h
#hahahaha
