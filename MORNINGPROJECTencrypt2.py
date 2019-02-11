print(ord("a"))

message = input("Enter a message to encrypt: ").upper()
encrypted = ""

for letter in message:
    if letter == " ":
        encrypted += " "
    #Make sure that the encrypted password include only normal character like a,b,C,D
    elif ord(letter) + 5 > ord("Z"):
        encrypted += chr(ord(letter)+ 5 -26)
    else:
        encrypted += chr(ord(letter) + 5)

print(encrypted)