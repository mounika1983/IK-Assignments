
# input values to list
list1 = [12, 3, 4, 15, 20]

for elem in list1:
    print(elem)

list1.sort()

print(list1)

colors = ["Red", "Black", "Pink", "White"]

colors.append("Blue")  # add --> insert
colors.append("Orange")

for color in colors:
    print(color)


print(len(colors))

for i in range(len(colors)):
    print(colors[i])

if "Grey" in colors:
    print("Yes, present")


list2 = []

list2.append("Abc");

print(list2)