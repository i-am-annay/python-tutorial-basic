# Imports and Executes specified attributes only
from my_modules import find_index, test1

courses = ['History', 'Math', 'Physics', 'CompSci']
index = find_index(courses, 'Math')
print(index)
print(test1)
# print(test2)      Error because test2 is not imported
