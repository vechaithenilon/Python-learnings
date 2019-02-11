import random

VOWEL = ('a','e','i','o','u','A','E','I','O','U')  #Tuple

message = input('Enter your message here: ')

new_message = ''

for letter in message:
    if letter not in VOWEL:
        new_message += letter
    else:
        temp = random.choice(VOWEL)
        while temp == letter:
            temp = random.choice(VOWEL)
        else:
            new_message += temp

print('THere you go, a silly random generated message')
print (new_message)

