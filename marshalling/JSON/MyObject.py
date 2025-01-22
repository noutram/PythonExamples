import json

# Create a class with two properties: name and age.

class Person:
    # __init__ is a special method used to initialize the object's properties.
    def __init__(self, name, age): 
        self.name = name           
        self.age = age
    # __repr__ is a special method used to represent a class's objects as a string.
    def __repr__(self):             
        return f'Person(name={self.name}, age={self.age})'
    # Serialize the object to a JSON formatted string.
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__) 
    # Function to create an instance by deserializing a JSON formatted string.
    @staticmethod
    def from_json(json_text):
        return json.loads(json_text, object_hook=lambda d: Person(**d))
    # Function to update the object's properties from a JSON formatted string.
    def update_from_json(self, json_text):
        data = json.loads(json_text)
        self.name = data['name']
        self.age = data['age']

# Create an object of the class
p = Person('John', 30)

# Write to terminal
print(p)

# Serialize
json_text = p.to_json()
print(f'JSON: {json_text}')

# Save to file person.json
with open('person.json', 'w') as f:
    f.write(json_text)

# Load from file
with open('person.json', 'r') as f:
    json_text = f.read()

# Deserialize using static method
p2 = Person.from_json(json_text)
print(f'Deserialized: {p2}')

