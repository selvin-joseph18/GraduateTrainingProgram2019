'''Write a function isIn() that accepts two strings as arguments and returns
True if either string occurs anywhere in the other, and False otherwise.
Hint: you might want to use the built-in str operation in.'''


def isln(s1,s2):
    if (s1 in s2) or (s2 in s1):
        return True
    else:
        return False

s1 = input("enter first string: ")
s2 = input("enter second string: ")

result = isln(s1,s2)
print(result)