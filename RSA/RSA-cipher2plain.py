#!/usr/bin/python

p = int(input("Enter p: "))
ct = int(input("Enter ciphertext: "))
e = int(input("Enter e: "))
n = int(input("Enter n: "))
q = n // p
from Crypto.Util.number import inverse
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
pt = pow(ct, d, n)
print(pt)
