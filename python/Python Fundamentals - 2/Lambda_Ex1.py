def add_1(a, b):
    return a + b

c = add_1(5, 10)
print(c)

add_2 = lambda a,b: a + b

d = add_2(10,20)
print(d)

print(type(add_1))
print(type(add_2))

def greet1():
    print("Hello World")

greet = lambda : print('Hello World')

greet()

greet2 = lambda name: print("Hi " + name)

greet2("Matt")

print((lambda x: x + x)(2))


func = lambda a, b: (
    b - a if a <= b else
    a * b
)

print(func(10, 2))