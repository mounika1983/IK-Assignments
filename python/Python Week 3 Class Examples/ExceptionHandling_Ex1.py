# Syntax Error
'''
Syntax Error: As the name suggests this error is caused by the wrong syntax in the code. It leads to the termination of the program.

Exceptions: Exceptions are raised when the program is syntactically correct, but the code results in an error. This error does not stop the execution of the program, however, it changes the normal flow of the program.

'''

a = 5

print(a)

b = 0

try:
    print(a/b)

except:
    print("Error")


print("Matt")
print("Sam")





try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")

x = 5

try:
    x = x + "abc"

except Exception as e:
    print("Error: Something went wrong")
    print(e)

print(x)

print(1000)
print(2000)


