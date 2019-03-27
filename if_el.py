#!/usr/bin/env python
# coding=utf-8

def compare(a, b):
    print "compare(%d, %d)" % (a, b)
    if a == b :
        print "\ta == b is true"
        print "\ta = b = %d" % a
    elif abs(a - b) == 1 :
        print "\tabs(a - b) is true"
        print "\tabs(%d - %d) = 1" % (a, b)
    else :  
        print "\tabs(a - b) >= 2 is true"
        print "\tabs(%d - %d) >= 2" % (a, b)


compare(1, 1)
compare(1, 2)
compare(1, 3)
