
animals = ['cat', 'dog', 'pig', 'dog']
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

prime_numbers = [2, 3, 5, 7, 9, 11]

# remove all elements
prime_numbers.clear()

# Updated prime_numbers List
print('List after clear():', prime_numbers)

# Output: List after clear(): []