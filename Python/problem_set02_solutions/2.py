'''A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a function called is_power that takes parameters a and b and
returns True if a is a power of b. Note: you will have to think about the base case.
'''
def is_power(a,b):
    if a<b:
        return False
    if a==b:
        return True
    else:
        return is_power(a/b,b)


number1 = int(input("enter 1st number :"))
number2 = int(input("enter 2nd number: "))
result = is_power(number1,number2)
print(result)