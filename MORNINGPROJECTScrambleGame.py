# import random
# #Source code for jumbling process
# string = 'The quick brown fox jumped over the lazy dog'
# print(len(string))
# string = list(string) #Turn into a list previously a string
# jumbled = ''
#
# print(string)
#
# for letter in range(0, len(string)):
#     jumbled += string.pop(random.randint(0, len(string)-1))
#     print(len(string))
#     print(string)
#     print(jumbled)

#Making a jumble game?

import random

#Build word list
Wordlist = []
print('Pre-game: Please build your word list to play:')
while True:
    print('Please type your a single word you would like to add to the list(type nothing to start playing):')
    newword = str(input())
    # Add new word to the list
    if newword != '':
        Wordlist.append(newword)
        continue
    else:
        print('You have a list of ' + str(len(Wordlist))+ ' words')
        print('Now lets start')
        break


print('Welcome to the Jumble game, Please tell me what is this word?')

#choose a random word from the list
string = random.choice(Wordlist)
#Make a check later on
original = string

# Suggestion from Ngoc

jumbled = list(string)
random.shuffle(jumbled) #How to shuffle characters in a list
jumbled = ''.join(jumbled) #join randomized character into a word


# #Turn into a list previously a string to scramble
# string = list(string)
# # scramble the chosen word
# jumbled = ''
# for letter in range(0, len(string)):
#     jumbled += string.pop(random.randint(0, len(string)-1))

print(jumbled)

#Player input and comparison
while True:
    print('Write your answer here:')
    playerinput = input()
    print('You typed ' + playerinput)
    if playerinput != original:
        print('keep trying!')
        continue
    else:
        print('Nice job!')
        break

