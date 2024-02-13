def square(x):
    return (x*x)
def double(x):
    return (x+x)

funcs = [square, double] # list of functions

value = list(map(lambda x: x(10), funcs))
print(value)
