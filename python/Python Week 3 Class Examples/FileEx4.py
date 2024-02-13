# Appending to a file

file1 = open("test1.txt", "a")

file1.write("Writing at the end")

file1.close()


f = open("test2.txt", "r")
# move to 11 character
f.seek(11)
# read from 11th character
print(f.read())