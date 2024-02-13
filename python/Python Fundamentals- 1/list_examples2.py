
animals = ['cat', 'dog', 'guinea pig', 'dog']
animals.remove('dog')

print('Updated animals list: ', animals)

# error
#animals.remove('fish')

# Updated animals List
print('Updated animals list: ', animals)

# pop
languages = ['Python', 'Java', 'C++', 'French', 'C']

return_value = languages.pop(3)

print('Return Value:', return_value)

print('Updated List:', languages)

languages.pop()
print(languages)

# del

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# deleting the third item
del my_list[2]

# Output: [1, 2, 4, 5, 6, 7, 8, 9]
print(my_list)

# deleting items from 2nd to 4th
del my_list[1:4]

# Output: [1, 6, 7, 8, 9]
print(my_list)

# deleting all elements
del my_list[:]

# Output: []
print(my_list)

prime_numbers = [2, 3, 5, 7, 9, 11]

# remove all elements
prime_numbers.clear()

# Updated prime_numbers List
print('List after clear():', prime_numbers)


# Output: List after clear(): []