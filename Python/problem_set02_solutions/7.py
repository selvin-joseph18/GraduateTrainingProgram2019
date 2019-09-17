'''A palindrome is a word that is spelled the same backward and forward, like "Malayalam" and "Noon" .
Recursively, a word is a palindrome if the first and last letters are the same and the middle is a palindrome.
Write a function called is_palindrome that takes a string argument and returns True if it is a palindrome and False
otherwise. Remember that you can use the built-in function len to check the length of a string.
Use the function definition'''

'''def is_palindrome(s):
    if len(s)==1:
        print("palindrome")
    elif len(s) > 1:
        if s[0]==s[-1]:
            print('palindrome')
        else:
            print('not a palindrome')

string = input("enter the string: ")
is_palindrome(string)'''
                        # OR

def is_palindrome(s):
    rev =s[::-1]
    if s==rev:
        print('palindrome')
    else:
        print('not a palindrome')


string = input("enter the string: ")
is_palindrome(string)