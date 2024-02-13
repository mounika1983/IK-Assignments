'''

Writing to Files in Python
There are two things we need to remember while writing to a file.

1. If we try to open a file that doesn't exist, a new file is created.
2. If a file already exists, its content is erased, and new content is added to the file.
In order to write into a file in Python,
we need to open it in write mode by passing "w" inside open() as a second argument.

'''


with open('test5.txt', 'w') as file3:

    # write contents to the test2.txt file
    file3.write('Programming is Fun.')
    file3.write('Python for beginners')



'''
"x" – Create: this command will create a new file if and only if there is no file already in existence with that name or else it will return an error.
Example of creating a file in Python using the "x" command:

'''

#creating a text file with the command function "x"

f = open("test7.txt", "x")