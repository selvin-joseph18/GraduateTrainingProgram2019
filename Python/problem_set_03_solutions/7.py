'''rite a function named using_only() that takes a word and a string of letters, and that returns True if the word contains only letters in the list.
Can you make a sentence using only the letters acefhlo? Other than "Hoe alfalfa?"
'''

def using_only(word,string):

    for letter in word:
        if letter not in string:
         return False
    return True
word = 'tikkaaa'
string='tik'
result = using_only(word,string)
print(result)