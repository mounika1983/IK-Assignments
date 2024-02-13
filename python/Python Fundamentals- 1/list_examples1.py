# https://www.programiz.com/python-programming/methods/list

numbers = [21, 10, 54, 12]

print("Before Append:", numbers)

# using append method
numbers.append(32)
numbers.append(9)
print("After Append:", numbers)

prime_numbers = [2, 3, 5]
print(prime_numbers*2)

even_numbers = [4, 6, 8]
print("List2:", even_numbers)

prime_numbers.extend(even_numbers) # list1.extends(list2)

print("List after append:", prime_numbers)

languages = ['Python', 'Swift', 'C++']

languages[2] = 'C'

print(languages)  # ['Python', 'Swift', 'C']

# insert method
vowel = ['a', 'e', 'i', 'u']

# 'o' is inserted at index 3 (4th position)
vowel.insert(3, 'o')

print('List:', vowel)