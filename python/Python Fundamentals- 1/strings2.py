# .join() with lists
numList = ['1', '2', '3', '4']
separator = ', '
print(' | '.join(numList)) # "1 | 2 | 3, 4"

# .join() with tuples
numTuple = ('1', '2', '3', '4')
print(separator.join(numTuple))

s1 = 'abc'
s2 = '123'

# each element of s2 is separated by s1
# '1'+ 'abc'+ '2'+ 'abc'+ '3'
print('s1.join(s2):', s1.join(s2))

# each element of s1 is separated by s2
# 'a'+ '123'+ 'b'+ '123'+ 'b'
print('s2.join(s1):', s2.join(s1))

# first string
firstString = "PYTHON IS AWESOME!"

# second string
secondString = "PyThOn Is AwEsOmE!"

if(firstString.lower() == secondString.lower()):
    print("The strings are same.")
else:
    print("The strings are not same.")

sentence = "i love PYTHON"

mylist = sentence.split(" ")
for i in range(len(mylist)-1,-1,-1):
    if(len(mylist[i]) > 0):
        sentence = mylist[i]
        break
print(len(sentence))

# converts first character to uppercase and others to lowercase
capitalized_string = sentence.capitalize()

print(capitalized_string)

# Output: I love python


message = 'Python is fun'

print(message.startswith('Python'))


