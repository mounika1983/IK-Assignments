'''

Call by Reference in Python

When Mutable objects such as list, dict, set, etc.,
are passed as arguments to the function call,
it can be called Call by reference in Python.
When the values are modified within the function,
the change also gets reflected outside the function.

'''

def myFunc(myList):
    print(id(myList))
    print("List received: ", myList)
    myList.append(3)
    myList.extend([7, 1])
    print("List after adding some elements:", myList)
    myList.remove(7)
    print("List within called function:", myList)
    print(id(myList))


List1 = [1, 4, 10, 5]
print(id(List1))
print("List before function call :", List1)
myFunc(List1)
print("List after function call: ", List1)

