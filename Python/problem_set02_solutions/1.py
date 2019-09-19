'''The greatest common divisor (GCD) of a and b is the largest number that divides both of them with no remainder.
One way to find the GCD of two numbers is based on the observation that if r is the remainder when a is divided by b, then gcd(a, b) =
gcd(b, r). As a base case, we can use gcd(a, 0) = a.
Write a function called gcd that takes parameters a and b and returns their greatest common divisor.'''


'''from math import *
result = gcd(15,20)
print(result)
                     OR       '''

def calculateGcd(number1,number2):
    if number2==0:
        return number1
    else:
        return calculateGcd(number2,number1%number2)


number1 = int(input("enter 1st number: "))
number2 = int(input("enter 2nd number: "))
gcd=calculateGcd(number1,number2)
print(gcd)