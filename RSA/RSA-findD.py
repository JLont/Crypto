#!/usr/bin/python

from Crypto.Util.number import inverse

q = int(input("Enter q: "))
p = int(input("Enter p: "))
e = int(input("Enter e: "))
tort = (p - 1) * (q - 1)
d = inverse(e, tort)
prind(d)
