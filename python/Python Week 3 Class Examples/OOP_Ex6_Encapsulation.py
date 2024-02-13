# Python program showing a use
# of get() and set() method in
# normal function

class Person:
    def __init__(self, name, age):
        self.name = name # public
        self._age = age  # private = non-public
        
    # getter method
    def get_age(self):
        if (self._age < 0):
            print("This is not a valid age")
            return -1
        return self._age

    # setter method
    def set_age(self, x):
        if x < 0:
            self._age = 0
        self._age = x


p1 = Person("Matt", 20)

p2 = Person("Raju", 30)

# setting the age using setter
p1.set_age(21)

# retrieving age using getter
print(p1.get_age())

print(p1._age)

p1._age = -50

print(p1._age)
