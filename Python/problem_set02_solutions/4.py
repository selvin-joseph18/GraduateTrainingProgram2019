'''Write a program that computes the decimal equivalent of the binary number 10011?'''

from math import *
def binary_decimal(b):
    return int(b,2)


n= 10011
b=str(n)
decimal=binary_decimal(b)
print(decimal)