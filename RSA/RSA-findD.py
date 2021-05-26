#!/usr/bin/python

from Crypto.Util.number import inverse

q = input("Enter q: ")
p = input("Enter p: ")
e = input("Enter e: ")
tort = (p - 1) * (q - 1)
d = inverse(e, tort)
prind(d)