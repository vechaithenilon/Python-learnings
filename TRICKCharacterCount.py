message = 'It was a bright cold day in April, and the clocks were striking thirteen'
count = {}

for character in message:
    count.setdefault(character,0)  #set the first value for string that has never appeared in dict rather than a KeyError message
    count[character] = count[character] + 1 #add up to the existing key values

print(count)

#Nice way to count characters in a message