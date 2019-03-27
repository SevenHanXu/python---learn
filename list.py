#!/usr/bin/env python
# coding=utf-8

list_a = [1, 2.2, "hello world", [1, 2, 3]]
list_b = ()
print "list_a = %s" % str(list_a)
print "list_b = %s" % str(list_b)

range_a = range(0, 100)
print "rang_a = %s" % str(range_a)
print type(range_a)

list_c = range(0, 5)
list_d = range(5, 10)

print "list_c = %s" % str(list_c)
print "list_d = %s" % str(list_d)

list_c.append(2.3)
print "list_c = %s" % str(list_c)

list_c.insert(3, [1, 2, 3])
print "list_c = %s" % str(list_c)

list_d.extend(list_c)
print "list_d = %s" % str(list_d)


del list_c[0]
print "list_c = %s" % str(list_c)
print "list_d = %s" % str(list_d)

list_c.pop(3)
print "list_c = %s" % str(list_c)
print "list_d = %s" % str(list_d)

list_e = range(0, 10, 2)
print "list_e = %s" % str(list_e)

list_f = range(0, 11)
print "list_f [2~5] = %s" % str(list_f[2 : 6])
print "list_f [2~the last num] = %s" % str(list_f[2 : ])
print "list_f [2~倒数第二个元素] = %s" % str(list_f[2 : -1]) #下标为2
print "list_f [全部元素] = %s" % str(list_f[ : ])
print "list_f [全部元素:每隔两个取一个元素] = %s" % str(list_f[ : : 2])


import random
list_g = [random.randint(0, 10) for x in xrange(0, 10)]
print "list_g = %s" % str(list_g)
sorted(list_g)
print "list_g = %s" % str(list_g)
list_h = sorted(list_g)
print "list_h = %s" % str(list_h)
list_g.sort(reverse = True)
print "list_g = %s" % str(list_g)
