grid = [['.' , '.' , '.' , '.' , '.', '.' ],
        ['.', '1', '2', '.', '.', '.'],
        ['3', '4', '5', '6', '.', '.'],
        ['7', '8', '9', '10', '11', '.'],
        ['.', '13', '14', '15', '16', '12'],
        ['17', '18', '19', '20', '27', '.'],
        ['21', '22', '23', '24', '.', '.'],
        ['.', '25', '26', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# print(grid[2][0])
# print(grid[3][1])
print(len(grid[0])) #Get the number of value in each row
print(len(grid))    #Get the number of columns


#Change the values to 0
for j in range(len(grid[0])):
    for i in range(len(grid)):
        if grid[i][j] != '.':
            grid[i][j] = '0'


for j in range(len(grid[0])):
    for i in range(len(grid)):
        print(grid[i][j],end='')
    print('') #create new line

#LEARNINGS:
#1. how to get the number of values in a row
#2. how to get a number of columns
#3. how to make a line break with print(....., end='' and a print at the end of the small loop)










