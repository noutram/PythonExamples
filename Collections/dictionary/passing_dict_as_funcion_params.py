# function fred that takes two parameters, and an optional third
def funcWithSeparateParams(name, age, sn = 0):
    print(f'Name: {name}, Age: {age}, Serial: {sn}')

# Create a dictionary
test_dict = {'name': 'John', 'age': 30}
# Call the function with the dictionary instead of separate parameters
funcWithSeparateParams(**test_dict)

# Create a dictionary with all three parameters
test_dict = {'name': 'Jane', 'age': 25, 'sn': 123}
funcWithSeparateParams(**test_dict)