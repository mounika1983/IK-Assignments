import operator
from operator import attrgetter

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

# employees.sort(key=attrgetter('name'))

# output: [{Joe, Finance, 25}, {John, IT, 28}, {Sam, Banking, 20}]
print(employees)


def getAge(employee):
    return employee.age

# employees.sort(key=getAge)

# employees.sort(key = lambda e: e.age)

print(employees)
