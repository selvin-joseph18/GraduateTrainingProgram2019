'''Write a function called is_abecedarian that returns True if the letters in a word appear in alphabetical order (double letters are ok).
How many abecedarian words are there? (i.e)
"Abhor" or "Aux" or "Aadil" should return "True" Banana should return "False"'''


def is_abecedarian(word):
    for i in range(len(word)-1):
        if word[i] > word[i+1]:
            return False
        else:
            return True

word = 'adhil'
result =  is_abecedarian(word)
print(result)