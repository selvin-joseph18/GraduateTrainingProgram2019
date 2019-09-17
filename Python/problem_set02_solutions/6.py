'''def findAnEven(l):
    try:
        for i in l:
            if i%2==0:
                return i
                break
    except ValueError as ve:
        print("no even numbers entered")

l = [1,5,2]
res = findAnEven(l)
print(res)'''

def findEven(L):
    try:
        for num in L:
            if num%2==0:
                return num
        
    except:
        raise ValueError

l=[1,5,3,7]
res=findEven(l)
print(res)