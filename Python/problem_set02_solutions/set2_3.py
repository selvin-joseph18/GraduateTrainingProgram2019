def factI(number):
    fact = 1
    if number == 0 or number == 1:
        return 1
    else:
        for i in range(2,number+1):
            fact = fact * i
        return fact

def factR(number):

    if number == 0:
        return 1
    else:
        return number * factR(number-1)

number  = int(input('Enter a number :'))
resultI = factI(number)
resultR = factR(number)
print(resultI)
print(resultR)