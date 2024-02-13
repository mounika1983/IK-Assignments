# https://www.freecodecamp.org/news/object-oriented-programming-in-python/\

# How to create a class:

class Student:

    def walk(self):
        print("Hey, I am walking")


student1 = Student() # create an object

student1.walk()

s2 = Student()

student1.name = "Matt"
student1.age = 25

s2.cgpa = 3.5
print(s2.cgpa)

print(student1.name)
