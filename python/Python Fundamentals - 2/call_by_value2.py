
'''
Call by Value in Python

When Immutable objects such as whole numbers, strings, etc are passed as arguments
to the function call, then it can be considered as Call by Value.

This is because when the values are modified within the function,
then the changes do not get reflected outside the function.

'''


def myFunc(a):
    print(id(a))
    print("Value received in 'a' =", a)
    a += 2
    print(id(a))
    print("Value of 'a' changes to :", a)


num = 13
print(id(num))
print("Initial number: ", num)
myFunc(num)
print("number after fun call= ", num)
