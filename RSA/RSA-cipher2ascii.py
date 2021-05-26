#!/usr/bin/python

m = input("Enter m: ")
x = (bytes.fromhex(format(m,'x'))).decode('utf-8')
print(x)