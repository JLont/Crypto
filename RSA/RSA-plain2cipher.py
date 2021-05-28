#!/usr/bin/python

from Crypto.Util.number import inverse

pt = int(input("Enter plaintext: ")) 
e = int(input("Enter e: "))
n = int(input("Enter n: "))
ct = pow(pt, e, n)
print(ct)
