"""
Contains the Person class which represents a person.
"""
import json

class Person:
    """
    A class to represent a person.

    Attributes:
    ----------
    name : str
        name of the person
    age : int
        age of the person
    """
    def __init__(self, name, age): 
        """
        Constructs all the necessary attributes for the person object.

        Parameters:
        ----------
        name : str
            name of the person
        age : int
            age of the person
        """
        self.name = name           
        self.age = age

    def __repr__(self):             
        """
        Returns a string representation of the person object.

        Returns:
        -------
        str
            string representation of the person object
        """
        return f'Person(name={self.name}, age={self.age})'

    def to_json(self):
        """
        Serializes the person object to a JSON formatted string.

        Returns:
        -------
        str
            JSON formatted string
        """
        return json.dumps(self, default=lambda o: o.__dict__, indent=4) 

    @staticmethod
    def from_json(json_text):
        """
        Creates an instance of Person by deserializing a JSON formatted string.

        Parameters:
        ----------
        json_text : str
            JSON formatted string

        Returns:
        -------
        Person
            an instance of Person
        """
        return json.loads(json_text, object_hook=lambda d: Person(**d))

    def update_from_json(self, json_text):
        """
        Updates the person's attributes from a JSON formatted string.

        Parameters:
        ----------
        json_text : str
            JSON formatted string
        """
        data = json.loads(json_text)
        self.name = data['name']
        self.age = data['age']


if __name__ == '__main__':
    # Create an object of the class
    p = Person('John', 30)

    # Write to terminal
    print(p)

    # Serialize
    json_text = p.to_json()
    print(f'JSON: {json_text}')

    # Save to file person.json
    with open('person.json', 'w', encoding="utf-8") as f:
        f.write(json_text)

    # Load from file
    with open('person.json', 'r', encoding="utf-8") as f:
        json_text = f.read()

    # Deserialize using static method
    p2 = Person.from_json(json_text)
    print(f'Deserialized: {p2}')

    # Update from JSON
    p.update_from_json('{"name": "Alice", "age": 25}')
    print(f'Updated: {p}')