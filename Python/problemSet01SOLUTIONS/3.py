'''Write a program that asks the user to input 10 integers, and
then prints the largest odd number that was entered. If no odd number was entered,
it should print a message to that effect.
'''


n = int(input("enter the number of elements: "))
list1=[]
c=0
for i in range(n):
    i = int(input("enter the number :"))
    if i%2!=0:
        list1.append(i)
    else:
        c+=1
if c==n:
    print('no odd numbers')
else:
    list1.sort()
    print(list1[-1])
