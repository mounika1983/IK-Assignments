'''
Python variables are not storage containers.
Rather Python’s variables are like memory references.
They refer to the memory address where the value is stored.
'''

x = 5

print("id of x =", id(x))

y = 10

print("id of y =", id(y))

x = 20

print("id of x =", id(x))

x = "abc"
print("id of x =", id(x))
k = x
print("id of k =", id(k))

k = 10
print("x =", x)
print("k = ", k)
print("id of x =", id(x))
print("id of k =", id(k))

p = "abc"
print("id of p =", id(p))

a = 10
print(id(a))
a = a + 5
c = 20-5
print(id(a))
print(id(15))
print(id(c))

l1 = [1, 2, 3]

l2 = [1, 2, 3]

print(id(l1))
print(id(l2))

'''
Immutable: tuples, int, str, bool 

Mutable: list, set, dict 
'''