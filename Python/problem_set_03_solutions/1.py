def is_palindrome(s):
    res= s== s[::-1]
    return res

s = 'mom'
res=is_palindrome(s)
print("is the string palindrome :" ,res)