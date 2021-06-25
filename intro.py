# **** Lesson 5: If-Else, Conditions, Booleans****
# If - Syntax
language = 'Python'
if language == 'Python':
    # print('Language is python') <- This gets printed
    pass
elif language == 'Java':
    # print('Language is Java')
    pass
else:
    # print('Language is not matched')
    pass
# Logical Operators
# and
# or
# not

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    # print('Welcome admin') <- This Gets printed
    pass

if user == 'Admin' or logged_in:
    # print('Welcome') <- This gets printed
    pass

if not (user == 'Admin' or logged_in):
    # print('Hello guest') <- This does not get printed
    pass

# ****Object Identity Checker****
a = [1, 2, 3]
b = [1, 2, 3]

c = [3, 4, 5]
d = c

str1 = 'Annay'
str2 = 'Annay'
str3 = str1
condition1 = (id(a) == id(b))   # Different objects in memory -> False (*)
condition2 = (a == b)           # Same objects in value       -> True
condition3 = (id(c) == id(d))   # Same objects in memory      -> True
condition4 = (c == d)           # Same objects in value       -> True

condition5 = (id(str1) == id(str2))  # Same objects in memory -> True (*)
condition6 = (str1 == str2)          # Same objects in value  -> True
condition7 = (str1 == str3)          # Same objects in value  -> True
condition8 = (id(str3) == id(str2))  # Same objects in memory -> True


# Note: id() -> method returns the unique identity of the object
# Note: (*) immutable objects are created once and have a fixed id for all variables
# Note: (*) mutable objects are created with each unique assingment and have a different id for different variables
