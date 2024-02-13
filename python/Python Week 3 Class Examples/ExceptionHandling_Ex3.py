 
    
    

pos1 = int(input())
pos2 = int(input())
try:
    result = pos1 / pos2
    print(result)
except:
    print("Error: Denominator cannot be 0.")
else:
    print("result: ", result)
finally:
    print("This is finally block.")
