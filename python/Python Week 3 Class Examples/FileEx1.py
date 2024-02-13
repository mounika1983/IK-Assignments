# # open a file
# file1 = open("test1.txt", "r")

# # read the file
# content = file1.read()

# print(type(content))
# print(content)

# file1.close()


# with open("test2.txt", "r") as file2:
#     content = file2.read()
#     print(content)


content= " mouni is a very good girlsgfgghh"
content = content.strip().split(" ")



i =0
result = ""

for n in content:
	if (len(n) > i):
		i = len(n)
        result = n
print(result)
