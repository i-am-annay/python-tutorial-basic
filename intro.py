# ****Lesson 4: Dictionaries****

student = {'name': 'Jhon', 'age': 23, 'courses': [
    'Math', 'Science'], 14: 'this is 14'}

# ****Accessing Values****
# Manually
student['name']     # Returns the corresoponding value
# student['grade']    # Throws an error when key doesn't exist

# Via Method
student.get('name')                 # Returns the corresoponding value
student.get('grade')                # Returns 'None' when key not found
student.get('grade', 'Not Found')   # Returns 'Not found' when key not found

# ****Updating Values*****
# Manually
student['grade'] = 3.8              # Adds/updates key-value

# Via method
student.update({'address': '321 python lane, rossum road',
                'phone': '2211', 'age': 22})

# ****Removing Values****
del student['address']  # Removes the specific key-value pair
student.pop('phone')    # Removes the specific key-value pair
# student.pop()           # Error, at least 1 argument needed

# ****Looping through Dicitonaries****
# Default -> Access only the keys
for key in student:
    # print(key)
    pass

# Explicit -> Access only the keys
for key in student.keys():
    # print(key)
    pass

# Explicit -> Access only the values
for value in student.values():
    # print(value)
    pass

# Explicit -> Access both
for key, vaulue in student.items():
    # print(key, value)
    pass

# ****Getting length, keys, values and pairs****
len(student)        # Returns length
student.keys()      # Returns 'dict_keys' object
student.values()    # Returns 'dict_values' object
student.items()     # Returns 'dict_items' object
