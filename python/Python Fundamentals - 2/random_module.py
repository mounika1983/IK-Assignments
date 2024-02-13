# https://www.w3schools.com/python/module_random.asp

import random

print(random.randint(1, 20))

print(int(1000*random.random())) # 0.23

list1 = [1, 8, 3, 20, 5, 6]
print(random.choice(list1))

# prints a random item from the string
string = "Google"
print(random.choice(string))

random.shuffle(list1)

print(list1)

print(random.sample(list1, 2))

