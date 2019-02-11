spam = ['apples','bananas','tofu','cats','toys']

# def Commacode(list):
#     printedString = ''
#     for i in list:
#         printedString = printedString + str(i)
#         if list.index(i) == (len(list)-2):
#             printedString = printedString + ', and '
#         elif list.index(i) == (len(list)-1):
#             printedString = printedString
#         else:
#             printedString = printedString + ', '
#     return printedString
#
# print(Commacode(spam))




# print(Commacode(spam))


#https://stackoverflow.com/questions/38824634/automate-the-boring-stuff-with-python-comma-code

def Commacode(list):
    if len(list) == 1:
        return list[0]
    return '{}, and {}'.format(', '.join(list[:-1]), list[-1])
# The key thing to understand here is the ''.format(). Take a look and see how parallel the format for each side of the
# syntax
# {} is important because it use the newly created dictionary rather than an empty list of []
print(Commacode (spam[:2]))
print(Commacode(spam))

#LEARNINGS:
#Understand the format function