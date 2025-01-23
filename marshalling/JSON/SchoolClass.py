from Person import Person

class SchoolClass:
    """
A class to represent a school class.

Attributes:
----------
className : str
    The name of the class.
students : list
    A list to store students in the class.
teachers : list
    A list to store teachers in the class.

Methods:
-------
addStudent(student):
    Adds a student to the class.
addTeacher(teacher):
    Adds a teacher to the class.
printClass():
    Prints the class name, students, and teachers.
"""
    def __init__(self, className):
        self.className = className
        self.students = []
        self.teachers = []

    def addStudent(self, student):
        self.students.append(student)

    def addTeacher(self, teacher):
        self.teachers.append(teacher)

    def printClass(self):
        print("Class: " + self.className)
        print("Students:")
        for student in self.students:
            print(student)
        print("Teachers:")
        for teacher in self.teachers:
            print(teacher)