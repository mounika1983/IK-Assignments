class Employee:

    def __init__(self, name, dept, age):
        self.name = name
        self.dept = dept
        self.age = age

    def __repr__(self):
        return '{' + self.name + ', ' + self.dept + ', ' + str(self.age) + '}'



employees = [
        Employee('John', 'IT', 28),
        Employee('Sam', 'Banking', 20),
        Employee('Joe', 'Finance', 25)
]

print(employees)

# cmp - HW

    # sort list by `name` in the natural order
employees.sort(key = lambda x: x.name)

print(employees)

#employees.sort(key=lambda x: x.name, reverse=True)

#print(employees)

