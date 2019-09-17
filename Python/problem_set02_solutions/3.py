
'''Observe the following function definitions. They Calculate the Factorial as per the Mathematical definition 1! = 1 (n + 1)! = (n + 1) * n!
Implement factI(n) as an Iterative Implementation & factR(n) as a Recursive Implementation
'''
def facI(n):
    fact=1
    if n==0 or n==1:
        return 1
    else:
        for i in range(1,n+1):
          fact = fact *i
    return fact

def factR(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factR(n-1)
n = int(input("enter a number to find factorial : "))
fact = factR(n)
print(fact)