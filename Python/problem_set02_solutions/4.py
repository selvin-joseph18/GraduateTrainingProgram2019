'''Write a program that computes the decimal equivalent of the binary number 10011?'''

from math import *
def binary_decimal(binary):
    return int(binary,2)


number= 10011
binary=str(number)
decimal=binary_decimal(binary)
print(decimal)