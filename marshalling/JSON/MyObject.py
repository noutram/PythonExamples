# Create a class with two properties: name and age.

class Person:
    # __init__ is a special method used to initialize the object's properties.
    def __init__(self, name, age): 
        self.name = name           
        self.age = age
    # __repr__ is a special method used to represent a class's objects as a string.
    def __repr__(self):             
        return f'Person(name={self.name}, age={self.age})'
    

# Create an object of the class
p = Person('John', 30)

# Write to terminal
print(p)
