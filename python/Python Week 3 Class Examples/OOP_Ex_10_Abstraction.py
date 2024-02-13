from abc import ABC, abstractmethod

class Animal(ABC): # abstract class

    @abstractmethod
    def sleep(self):
       pass

    def run(self):
        print("Running")


# derived class
class Dog(Animal):

    def bark(self):
        print("I can bark! Woof woof!!")

    def eat(self):
        print("Eating like a dog")

    def sleep(self):
        print("sleeping like a dog")


# Create object of the Dog class
dog1 = Dog()

# Calling members of the base class
dog1.eat()
dog1.sleep()

# Calling member of the derived class
dog1.bark();
dog1.run();


