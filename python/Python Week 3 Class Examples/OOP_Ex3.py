class Student:

    def __init__(self, age, name, cgpa):
        print("Creating a student object")
        self.age = age
        self.name = name
        self.cgpa = cgpa

    def study(self):
        print("I am learning something")


    def __repr__(self):
        return "Student object "+ self.name


class Course:

    def __init__(self, name):
        self.name = name
        self.list_of_learners = []

    def add_a_student(self, stud_obj): # enroll
        self.list_of_learners.append(stud_obj)

    def find_topper(self):
        max_cgpa = 0
        topper = None
        for stud in self.list_of_learners:
            if stud.cgpa > max_cgpa:
                max_cgpa = stud.cgpa
                topper = stud

        return topper



student1 = Student(25, "Matt", 4)
student2 = Student(28, "Sachin", 3)

math_course = Course("Math")
print(math_course)

math_course.add_a_student(student2)
math_course.add_a_student(student1)

print(math_course.find_topper())

