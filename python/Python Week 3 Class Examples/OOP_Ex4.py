class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__(self):
        print("deleting this object"+ self.name)

    def __repr__(self):
        return '{' + self.name + ', ' + str(self.salary) + '}'



emp1 = Employee("Matt", 2000)

emp2 = Employee("Raju", 5000)
emp1.displayEmployee()
emp2.displayEmployee()

print(emp2)
print("Total Employee %d" % Employee.empCount)

print(hasattr(emp1, 'salary') )   # Returns true if 'salary' attribute exists
print(getattr(emp1, 'salary'))   # Returns value of 'salary' attribute
print(setattr(emp1, 'salary', 7000)) # Set attribute 'salary' at 7000
print(delattr(emp1, 'salary') )   # Delete attribute 'salary'