def sumDigits(s):
    new_list = []
    try:
        for i in s:
            if i.isdigit():
                new_list.append(int(i))
        print(sum(new_list))

    except TypeError as te:
        print('please enter a string \n',te)
string = '1a2'
sumDigits(string)

