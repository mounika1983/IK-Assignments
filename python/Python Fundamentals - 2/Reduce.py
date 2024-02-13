# python code to demonstrate working of reduce()

# importing functools for reduce()
import functools

# initializing list
lis = [1, 3, 5, 6, 2]

# using reduce to compute sum of list
print(functools.reduce(lambda a, b: a + b, lis))

def product(x,y):
    return x*y

ans = functools.reduce(product, [2, 5, 3, 7])
print(ans)

