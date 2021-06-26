# Imports and Executes specified attributes only
from my_modules import find_index as fi, test1 as t1

courses = ['History', 'Math', 'Physics', 'CompSci']
index = fi(courses, 'Math')
print(index)
print(t1)
# print(test2)      Error because test2 is not imported
