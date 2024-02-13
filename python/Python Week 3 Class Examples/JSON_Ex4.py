import json


class Laptop:
    def __init__(self, name, processor, hdd, ram, cost):
        self.name = name
        self.processor = processor
        self.hdd = hdd
        self.ram = ram
        self.cost = cost


# create object
laptop1 = Laptop('Dell Alienware', 'Intel Core i7', 512, 8, 2500.00)

# convert to JSON string

dict1 = laptop1.__dict__

print(dict1)

jsonStr = json.dumps(dict1)

# print json string
print(jsonStr)