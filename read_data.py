#!/usr/bin/env python
# coding=utf-8


#a = raw_input("Please input:")
#print "a = ", a
#b = int(raw_input("Please input integer:"))
#print "b = ", b + 4

c , d = [int(x) for x in raw_input("Please input integer : ").split()]
print "c + d = ", c + d
print "%d + %d = " % (c , d), c + d
