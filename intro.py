# ****Lesson 3: Lists, Tuples, Sets****
# ##### LISTS #####
course = ['History', 'Mathematics', 'Science', 'Computer Science']

# ****Accessing Values and Length of the List****
len(course)
course[0]               # Gets the Item at the 1st index
course[2]               # Gets the Item at the 3rd index
course[len(course)-1]   # Gets the Item at the last index
course[-1]              # Gets the Item at the last index
course[0:2]             # Gets the Items from 1st to 2nd index
course[:2]              # Gets the Items from 1st to 2nd index
course[2:]              # Gets the Items from 3rd to the last

# ****Adding items into a list****
course.append('Art')            # Adds the item at the end
course.insert(3, 'Sociology')   # Inserts the item at the specific index

basic_science = ["Physics", 'Chemistry', 'Biology']
course.insert(0, basic_science)  # Inserts the list at the specific index
course.append(basic_science)     # Adds the list at the end
course.extend(basic_science)     # Adds elements from the second list

# ****Removing items from the list****
course.remove(basic_science)    # Removes the specified item
course.pop()                    # Removes and returns the last item
course.remove(basic_science)    # Removes the specified item

# ****List Methods****
course.reverse()    # Reverses a given list (in-place)

nums = [4, 5, 1, 3, 2]
nums.sort()         # Sorts a given list in ascending order (in-place)
course.sort()       # Sorts a given list in alphabetical order (in-place)
# Returns a new sorted list (not in-place and built-in)
nums_sorted = sorted(nums)

# ****List Methods 2****
course.index('Sociology')   # Returns index of the item
# course.index('BBS')         # Throws error, item not present
'BBS' in course             # Returns True/False

# ****Looping through Lists****
for item in course:
    # print(item)
    pass

for index, item in enumerate(course):  # For getting indexes
    # print(index, item)
    pass

# ****Joining and Splitting Lists into strings****
course_str = ', '.join(course)      # Joins items on the string
course_str = '-'.join(course)       # Joins items on the string
new_course = course_str.split('-')  # Splits items on the string

# ****List Memory Allocation and Mutability****
list_1 = [1, 2, 3, 4]
list_2 = list_1

# print(list_1)
# print(list_2)
list_1[0] = 5

# print(list_1)
# print(list_2)

# Note: lists are mutable(changeable) and in the above example both list_1 and list_2 are same objects hence changing one list changes the other

# ##### TUPLES #####
# Note: Tuples are similar to lists
# But, they are immutable and do not support list methods that mutate the list

names_1 = ('Jhon', 'Jane', 'Ryu', 'Mario')
names_2 = names_1

# names_1[0] = 'Simon' --> Not Allowed in tuples


# ##### SETS #####
cs_courses = {'Math', 'Physics', 'Operating Systems',
              'Programming', 'Physics', 'Math'}  # Removes Duplicates
cse_courses = {'Math', 'Physics', 'Programming'}

# ****Intersection, Union Differenct****
print(cs_courses.intersection(cse_courses))
print(cs_courses.difference(cse_courses))
print(cs_courses.union(cse_courses))


# Empty lists
empty_list = []
empty_list = list()

# Empty tuples
empty_tuples = ()
empty_tuples = tuples()

# Empty sets
empty_sets = set()
empty_sets = {}  # NOT AN EMPTY SET ---> BUT A DICTIONARY
