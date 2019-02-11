birthdays = {'chi Truc': '7 Aug', 'Nhat Quang': '9 Aug', 'Tan WAND': '22 Aug', 'Trang VGU': '16 Jun', 'My VGU': '11 Oct',
            'Phuc WAND': '5 Nov', 'Thanh VGU': '18 Nov', 'Phuc VGU': '2 Dec', 'Nach VGU': '5 Dec', 'Nguyen VGU': '16 Mar',
            'Phat VGU': '4 Apr', 'Phuong WAND': '27 Mar'}

print('Welcome to birthdays list, here are the birthdays I have')

for v in birthdays.keys():
    print(v)

print('')


while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated')
        print('Do you want to see the entire new list? (Y or N)')
        answer = input()
        if answer == 'Y':
            for v in birthdays.keys():
                print(v)
