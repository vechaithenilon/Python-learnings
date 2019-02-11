import os

os.chdir('D:\Games\Vanq\Temp')

print(os.getcwd())

for f in os.listdir():

    f_name, f_ext =(os.path.splitext(f)) #Separate file_name and extention

    f_title, f_num= (f_name.split(' - '))     #Prequisite: all names must have the same format

    f_num = f_num.strip()     # Remove excess space in the name



    '''COMMMENT THIS LINE IN REAL RUN TO SAVE TIME!!!'''
    print('{}{}'.format(f_num, f_ext))


    '''UNCOMMENT THESE 2 LINES TO RUN THE PROGRAM!!!'''
    new_name = '{}{}'.format(f_num, f_ext)
    os.rename(f, new_name)


# ISSUE1: This requires user to change the directory of the the folder
# ISSUE2: The format of old name and new name need to be manually adjust to fit the intended usage
# ISSUE3: Limited modification: the program only allows user to move parts around, not changing any character inside
# ISSUE4: One time run only, after the name is changed, then a new set of sample is required