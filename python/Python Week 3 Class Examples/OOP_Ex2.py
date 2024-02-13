class Dog:

    def __init__(self, name, age, wt):   # constructor
        self.name = name
        self.age = age
        self.wt = wt
        print("Created a new dog object: " + name)

    def walk(self):
        print("I am walking: "+ self.name)

    def __del__(self):  # destructor
        print("deleting this object" + self.name)

    def __repr__(self):
        return "name: "+ self.name + "  wt: "+ str(self.wt)



dog1 = Dog("Tommy", 25, 5)

dog1.walk()

dog1.ht = 5

dog1.wt = 50

print(dog1)

print(dog1.ht)


dog2 = Dog("Sheru", 20, 15)

#print(dog2.is_alive)
#dog2.walk()


def fun(dog: Dog):
    print(dog.name)
    dog.name = "xyz"
    print(dog.name)


fun(dog2)

list1 = []

list1.append(dog1)
list1.append(dog2)

del list1[0]

print("list: ", list1)
