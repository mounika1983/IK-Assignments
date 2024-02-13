
class Dog:

    # constructor
    def __init__(self, name, wt):
        self.name = name
        self.wt = wt

    def speak(self):
        print("Barking")


# Dog dog1 = new Dog() - Java
dog1 = Dog("Tommy", 4.)

print(dog1.name)
print(dog1.wt)

dog1.color = "Blue"

print(dog1.color)

dog2 = Dog("Sheru", 5.2)

print(dog2.name)
print(dog2.wt)

dog2.speak()
