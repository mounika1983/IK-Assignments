# https://www.programiz.com/python-programming/dictionary

capital_city = {"Nepal": "Kathmandu", "Italy": "Rome", "England": "London"}
print(capital_city)

my_dict = {"name":"Max", "age":28, "city":"New York"}
print(my_dict)

# or use the dict constructor, note: no quotes necessary for keys
my_dict_2 = dict(name="Lisa", age=27, city="Boston")
print(my_dict_2)

print(capital_city["Nepal"])


capital_city["Japan"] = "Tokyo"
print("Updated Dictionary: ",capital_city)

#change a val
my_dict_2["age"] = 28
print(my_dict_2)

print(my_dict_2["age"])