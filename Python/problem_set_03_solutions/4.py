def has_no_e(words):
    old_list=words.split(" ")
    new_list=[]
    for word in old_list:
        if 'e' not in word:
            new_list.append(word)
    print(new_list)
    percentage = 100*(len(new_list)/100)
    print(percentage)


words = '''hello my name is selvin joseph and i'm currently working in accenture and i'm 21 year's old'''
has_no_e(words)
