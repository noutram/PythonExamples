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
        self.students = []  # Initialize as an empty list
        self.teachers = []  # Initialize as an empty list

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
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)
    
    # add static method to deserialize the class from JSON
    @staticmethod
    def from_json(json_text):
        """
        Deserializes a JSON formatted string to a SchoolClass object.
        Args:
            json_text (str): JSON formatted string
        Returns:
            SchoolClass: SchoolClass object
        """

        data = json.loads(json_text)
        school_class = SchoolClass(data['class_name'])
        school_class.students = [Person(**student) for student in data['students']]
        school_class.teachers = [Person(**teacher) for teacher in data['teachers']]
        return school_class
    

if __name__ == "__main__":

    # Create a new school class
    school_class1 = SchoolClass("Math Class")

    # Create a new student
    student1 = Person("Alice", 15)

    # Create a new teacher
    teacher1 = Person("Bob", 30)

    # Add the student and teacher to the class
    school_class1.add_student(student1)
    school_class1.add_teacher(teacher1)

    # Print the class details
    school_class1.print_class()

    print(student1.__dict__)
    print(teacher1.__dict__)
    print(school_class1.__dict__)

    # Serialize the class to JSON
    json_text1 = school_class1.to_json()

    # Save the JSON to a file
    with open("school_class1.json", "w", encoding="utf-8") as f:
        f.write(json_text1)

    # Load the JSON from the file
    with open("school_class1.json", "r", encoding="utf-8") as f:
        json_text2 = f.read()

    # Deserialize the class from JSON
    school_class2 = SchoolClass.from_json(json_text2)

    # Print the deserialized class details
    school_class2.print_class()

