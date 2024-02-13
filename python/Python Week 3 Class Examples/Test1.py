
class User:

    type = "abc"
    count = 0

    def __init__(self, age, name):
        self.name = name
        self.age = age
        User.count = User.count + 1

    def eat(self):
        User.type = "pqr"
        print("I am eating: ")
        print(User.type)

    def __repr__(self):
        return "name: + repr "+ self.name



user1 = User(20, "Raj")
user2 = User(30, "Matt")

print(user1.name)

user1.eat()

print(User.count)
print(user1.count)


print(user1.type)
print(user2.type)

