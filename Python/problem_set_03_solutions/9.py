'''Write a function called is_sorted that takes
a list as a parameter and returns True if the list is sorted in ascending order and False otherwise'''


def is_sorted(list1):
    for i in range(len(list1)-1):
        if list1[i] > list1[i+1]:
            return False
        else:
            return True

list1 = [1,2,3]
list2=['a','d','a','z']
result = is_sorted(list2)
print(result)