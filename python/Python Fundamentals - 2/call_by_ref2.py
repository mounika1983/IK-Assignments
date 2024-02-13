def myFunc(myList):
    print("List received: ", myList)
    myList.append(3)
    myList.extend([7, 1])
    print("List after adding some elements:", myList)
    myList.remove(7)
    print(id(myList))
    myList = [3, 4, 6]
    print(id(myList))
    print("List within called function:", myList)
    return


List1 = [1, 10, 8]
print("List before function call :", List1)
print(id(List1))
myFunc(List1)
print("List after function call: ", List1)
print(id(List1))
