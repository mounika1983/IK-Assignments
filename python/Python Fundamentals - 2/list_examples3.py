# create a list
numbers = [2, 3, 5, 2, 11, 2, 7]

count = numbers.count(2)

print('Count of 2:', count)

prime_numbers = [2, 3, 5, 7]

prime_numbers.reverse()

print('Reversed List:', prime_numbers)

prime_numbers = [11, 3, 7, 5, 2]

# sorting the list in ascending order
prime_numbers.sort()

print(prime_numbers)

vowels = ['e', 'a', 'u', 'o', 'i']

vowels.sort(reverse=True)
print('Sorted list (in Descending):', vowels)

l1 = [11, 3, 7, 5, 2]

l2 = l1

# l2 = l1.copy()

print(id(l1))
print(id(l2))

l2.append(9)

print(l1)
print(l2)