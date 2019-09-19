def findAnEven(list1):
    try:
        for number in list1:
            if number%2==0:
                print(number)
                exit()
        raise ValueError
    except ValueError as ve:
        print("please enter atleast one even number")


list1 = [1,3,5,4]
findAnEven(list1)
