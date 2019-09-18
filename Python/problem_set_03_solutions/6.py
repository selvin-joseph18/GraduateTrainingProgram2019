def avoids(word,f_letters):
    for letter in f_letters:
        if letter not in word:
            return True
    return False


f_letters=input("enter the forbidden letters : ")
words='''hi my name is selvin joseph and im 21 years old'''
count = 0
word_list = words.split(" ")
print(word_list)
for word in word_list:
    if avoids(word,f_letters):
        count+=1
print(count)
