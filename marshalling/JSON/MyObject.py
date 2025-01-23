from Person import Person

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
