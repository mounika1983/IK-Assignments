# https://www.programiz.com/python-programming/set


set1 = {1, 5, 10, 4, 6, 9, 19}

print(set1)
print(len(set1))
print(max(set1))

my_set = {"apple", "banana", "cherry"}
if "apple" in my_set:  # O(1)
    print("yes")

# print(set1[2])    --> error

# Creating a Set
people = {"Jay", "Matt", "Steph"}

print(people)

people.add("Raju")

for i in range(1, 6):
	people.add(i)

print(people)

numbers = {2, 4, 6, 6, 2, 8}
print(numbers)   # {8, 2, 4, 6}

companies = {'eBay', 'Fb'}
more_companies = ['apple', 'google', 'Fb']

companies.update(more_companies)

print(companies)

# Output: {'google', 'apple', 'Lacoste', 'Ralph Lauren'}