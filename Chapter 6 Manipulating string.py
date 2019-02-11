print("This is Alice's cat")

print('Say hi to Bob\'s mother')

print('Say hi to Lord\n of the money')

print('Get me a fucking\t tab!!!!')


print('Hello there!\nHow are you?\nI\'m doing fine')


print('''Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob''')

# THis part is a neat way to write comment which does not paint the entire program red!!!
'''This is a test PYthon program. 
Written by Al Sweigart

THis program was desinged for Python 3, not Python 10'''

# Indexing parts of a string
spam = 'Hello World!'
fizz = spam[0:5]
print(fizz)


spam = spam.upper()

print(spam)

print('How are you?')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too')
else:
    print('I hope the rest of your day is good')

print(spam.islower())

print(', '.join(['cats','rats','bats']))

SplitString = ''' Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment"

Please do not drink it.
Sincerely,
Bob'''

print(SplitString.split('\n'))
