"""
A module to represent a school class.
"""
import json
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
addStudent(student:Person):
    Adds a student to the class.
addTeacher(teacher:Person):
    Adds a teacher to the class.
printClass():
    Prints the class name, students, and teachers.
"""
    def __init__(self, class_name):
        """
        Initializes a new instance of the SchoolClass.
        Args:
            class_name (str): The name of the class.
        Attributes:
            class_name (str): The name of the class.
            students (list): A list of students in the class.
            teachers (list): A list of teachers in the class.
        """

        self.class_name = class_name
        self.students = [Person]
        self.teachers = [Person]

    def add_student(self, student: Person):
        """
        Adds a student to the class.
        Args:
            student (Person): The student to be added to the class.
        """
        self.students.append(student)

    def add_teacher(self, teacher: Person):
        """
        Adds a teacher to the list of teachers.
        Args:
            teacher (Person): The teacher to be added to the list.
        """
        self.teachers.append(teacher)

    def print_class(self):
        """
        Prints the details of the class including the class name, list of students, and list of teachers.
        This method prints the class name followed by the list of students and teachers associated with the class.
        """
        print("Class: " + self.class_name)
        print("Students:")
        for student in self.students:
            print(student)
        print("Teachers:")
        for teacher in self.teachers:
            print(teacher)

    # add function to serialize the class to JSON
    def to_json(self):
        """
        Serializes the SchoolClass object to a JSON formatted string.
        Returns:
            str: JSON formatted string
        """
        return json.dumps(self, default=lambda o: o.__dict__)