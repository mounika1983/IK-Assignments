#This program shows how to write data in a text file.

file = open("myfile2.txt","w")
L = ["This is Lagos \n","This is Python \n","This is Fcc \n"]

file.write("Hello There \n")
file.writelines(L)
file.close()


f = open("myfile2.txt", "r")
print(f.readline())

#print(f.readlines())