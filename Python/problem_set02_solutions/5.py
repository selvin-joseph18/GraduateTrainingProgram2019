'''Implement a function that meets the specification below. Use a try-except block.'''

def sumDigits(s):
    try:
        if isinstance(s, str):
            total = 0
            li = [x for x in s if x.isdigit()]
            for e in li:
                total += int(e)
        return total
    except:
        print("error" )
        exit()


s = 123
res=sumDigits(s)
print(res)
