VOWEL = ('a','e','i','o','u')  #Tuple

message = input('Enter your message here: ')

new_message = ''

for letter in message:
    if letter in VOWEL:
        print(letter, 'is a vowel') #the latter part is used to print the end of line with a space in between


    if letter not in VOWEL:
        # new_message = new_message + str(letter)
        new_message += letter

print (new_message)

