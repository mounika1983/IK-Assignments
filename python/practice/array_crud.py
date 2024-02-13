array = []

def addElement():
    n = int(input("how many number you want to enter:"))
    print('Enter elements: ')
    for i in range(n):
        array.append(int(input()))
    
    print('Given Array: ', array)
    
def addRangeElements():
    print('Enter element range to add: ')
    start = int(input())
    end = int(input())
    
    array.extend(range(start, end))
        
    print('Array with added elements: ', array)
    
def readElements():
    if(len(array) > 0):
        print('Enter position range to read: ')
        start = int(input())
        end = int(input())
        
        print('Elements at given range: ', array[start:end])
        
    else:
        print('Array is null')

    
def updateElement():
    if(len(array) > 0):
        index = int(input("Enter position to update:"))
        array[index] = int(input("Enter element to update:"))
        print('Array after update: ', array)
    
    else:
        print('Array is null')
    
def updateElements():
    if(len(array) > 0):
        print('Enter position range: ')
        pos1 = int(input())
        pos2 = int(input())
        print('Enter element range: ')
        start = int(input())
        end = int(input())
        array[pos1:pos2] = [*range(start, end, 1)]
        print('Array after update: ', array)
    
    else:
        print('Array is null')
    
def deleteElement():
    if(len(array) > 0):
        index = int(input("Enter position to delete element:"))
        del array[index]
        print('Array after delete element: ', array)
        
    else:
        print('Array is null')
    
def searchElement():
    if(len(array) > 0):
        index = int(input("Enter position to search:"))
        print('Element find at given position is: ', array[index])
    
    else:
        print('Array is null')
    
def sortArray():
    if(len(array) > 0):
        array = array.sort()
        print ('Sorted array: ', array)
        
    else:
        print('Array is null')
    
def sliceArray():
    if(len(array) > 0):
        print('Enter position to slice: ')
        pos = int(input())
        
        print('Left array: ', array[:pos])
        print('Right array: ', array[pos:])
    
    else:
        print('Array is null')
        
i = 0

while i < 11:   
    print()    
    print("1. Create an array")
    print("2. Read all elements from array")
    print("3. Read elements at given positions")
    print("4. Update an element from array")
    print("5. Update range of elements from array")
    print("6. Delete an element from array")
    print("7. Sort elements from array")
    print("8. Search element from array")
    print("9. sliceing the array")
    print("10. Add range of elements")
    
            
    i = int(input("Number you want to enter:"))
        
    if(i == 1):
        addElement()
    elif(i == 2):
        print(array[:])
    elif(i == 3):
        readElements()
    elif(i == 4):
        updateElement()
    elif(i == 5):
        updateElements()
    elif(i == 6):
        deleteElement()
    elif(i == 7):
        sortArray()
    elif(i == 8):
        searchElement()
    elif(i == 9):
        sliceArray()
    elif(i == 10):
        addRangeElements()
    else:
        break
