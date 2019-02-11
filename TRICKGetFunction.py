spam = {12345: 'Luggage Combination', 42: 'The Answer'}

#'12345' in spam.keys()
#'The Answer' in spam.values()

pinicItems = {'apples': 5, 'cups': 2}

print('I am bringing ' + str(pinicItems.get('cups',10)) + ' cups')
print('I am bringing ' + str(pinicItems.get('eggs',10)) + ' eggs')

#in get function, the number 10 helps the function return a value for key that does not exist in dict rather than an error message
