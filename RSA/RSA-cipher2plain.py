#!/usr/bin/python

p = input("Enter p: ")
ct = input("Enter ciphertext: ")
e = input("Enter e: ")
n = input("Enter n: ")
q = n // p
from Crypto.Util.number import inverse
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
pt = pow(ct, d, n)
print(pt)