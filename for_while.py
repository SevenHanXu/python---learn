#!/usr/bin/env python
# coding=utf-8

for i in xrange(0, 10000000):
    break

for i in range(0, 100):
    print i,
else:
    print "for end"


for i in range(0, 100):
    print i
    break
else:
    print "for end"

i = 10
while i:
    print "%d " % (i % 2),
    i /= 2
else:
    print "|finally num is %d" % i
