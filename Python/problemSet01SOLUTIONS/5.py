'''Write a program that asks the user to enter an integer and prints two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal
to the integer entered by the user. If no such pair of integers exists,
it should print a message to that effect.'''


'''from math import *
n = int(input("enter the number: "))
p=pow(n,5)
print(p)'''
'''import math
integer = 64

for power in range(1,6):
    a = (integer ** (1.0/power))
    if math.ceil(a) == a:
        print(a, power)'''
n=int(input("enter the number"))
c=0
for root in range(0,n):
    for pwr in range(1,6):
        if root ** pwr == n:
            c+=1
            print(root, pwr)
if c ==0:
    print('no pairs found')