#!/usr/bin/env python
# coding=utf-8

import random

#list_a = [random.randint(1, 100) for x in xrange(1, 10)]
list_a = [1, 3, 5]
print list_a

i = 1
for num in list_a:
    if num % 2 == 0:
        print "第%d个数是偶数%d" % (i, num)
        break
    else:
        i += 1
else :
    print "There is no even number"
