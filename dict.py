#!/usr/bin/env python
# coding=utf-8

dict_a = {
    (1, 2, 3) : "hello world!",
    "baidu" : "baidu.com",
    "haizei" : "haizeix.com"
    }
dict_b = dict()

print "dict_a = %s %s" % (str(dict_a), type(dict_a))
print "dict_b = %s %s" % (str(dict_b), type(dict_b))

for (key, value) in dict_a.items():
    print str(key) + ":=" + str(value)

for (key,value) in sorted(dict_a.items(), key = lambda x : x[1], reverse = True):
    print str(key) + ":=" + str(value)
print 2 + 3

dict_a["hrbin"] = "beer"
if not dict_a.has_key("baidu"):
    dict_a["baidu"] = "http://www.baidu.com"
dict_a.setdefault("baidu","http://www.baidu.com")
print "%s %s" % (str(dict_a), type(dict_a))
