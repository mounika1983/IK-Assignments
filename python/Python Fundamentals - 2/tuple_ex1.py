# https://www.programiz.com/python-programming/tuple

tuple_1 = ("Max", 28, "New York")
tuple_2 = "Linda", 25, "Miami" # Parentheses are optional

# Special case: a tuple with only one element needs to have a comma at the end,
# otherwise it is not recognized as tuple
my_tuple = (5)

print(type(my_tuple))

tuple_3 = (25,)
print(tuple_1)
print(tuple_2)
print(tuple_3)

# Or convert an iterable (list, dict, string) with the built-in tuple function
tuple_4 = tuple([1,2,3])
print(tuple_4)

#Error
#tuple_1[2] = "Boston"

for i in tuple_1:
    print(i)

if "New York" in tuple_1:
    print("yes")
else:
    print("no")


my_tuple = ('a','p','p','l','e',)

# len() : get the number of elements in a tuple
print(len(my_tuple))

# count(x) : Return the number of items that is equal to x
print(my_tuple.count('p'))

# index(x) : Return index of first item that is equal to x
print(my_tuple.index('l'))

# repetition
my_tuple3 = ('a', 'b') * 5
print(my_tuple3)

# repetition works on Lists and Strings also


# convert list to a tuple and vice versa
my_list = ['a', 'b', 'c', 'd']
list_to_tuple = tuple(my_list)
print(list_to_tuple)

tuple_to_list = list(list_to_tuple)
print(tuple_to_list)

# convert string to tuple
string_to_tuple = tuple('Hello')
print(string_to_tuple)
