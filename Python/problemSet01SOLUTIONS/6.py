'''Let s be a string that contains a sequence of decimal numbers separated by commas,
e.g., s = '1.23,2.4,3.123'. Write a program that prints the sum of the numbers in s.
'''
s = '1.23,2.4,3.123'
'''new_list=s.split(',')
total=0
for i in new_list:
    total+=float(i)
print(total)                     OR
'''
total = sum(map(float, s.split(",")))
print(total)
