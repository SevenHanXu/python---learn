#!/usr/bin/env python
# coding=utf-8

tuple_a = (1, 2, 3)
tuple_b = tuple([4, 5, 6]) #tuple函数可以将不是元组的元素转换成元组

print "tuple_a = %s %s" % (str(tuple_a), type(tuple_a))
print "tuple_b = %s %s" % (str(tuple_b), type(tuple_b))

print "tuple_a[1] = %s" % str(tuple_a[1])
print "tuple_a[1 : ] = %s" % str(tuple_a[1 : ])

print "tuple_a + tuple_b = %s" % str(tuple_a + tuple_b)

list_a = list(tuple_a)
list_a[1] = 9
tuple_a = tuple(list_a)
print "tuple_a = %s %s" % (str(tuple_a), type(tuple_a))
