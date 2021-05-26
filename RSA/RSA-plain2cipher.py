#!/usr/bin/python

from Crypto.Util.number import inverse

pt = input("Enter plaintext: ") 
e = input("Enter e: ")
n = input("Enter n: ")
ct = pow(pt, e, n)
print(ct)