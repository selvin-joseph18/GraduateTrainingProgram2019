'''Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn’t use any of the forbidden letters.'''


def avoids(word,f_letters):
    for letter in f_letters:
        if letter in word:
            return False
    return True

word='plzzzzzo'
f_letters='aeiou'
result=avoids(word,f_letters)
print(result)