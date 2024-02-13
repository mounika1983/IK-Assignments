odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

# union() : combine elements from both sets, no duplication
# note that this does not change the two sets
u_set = odds.union(evens)
print(u_set)

# intersection(): take elements that are in both sets
i = odds.intersection(evens)
print(i)

i = odds.intersection(primes)
print(type(i))
print(i)

i = evens.intersection(primes)
print(i)

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
# issubset(setX): Returns True if setX contains the set
print(setA.issubset(setB))
print(setB.issubset(setA)) # True

# issuperset(setX): Returns True if the set contains setX
print(setA.issuperset(setB)) # True
print(setB.issuperset(setA))

# isdisjoint(setX) : Return True if both sets have a null intersection, i.e. no same elements
setC = {7, 8, 9}
print(setA.isdisjoint(setB))
print(setA.isdisjoint(setC))