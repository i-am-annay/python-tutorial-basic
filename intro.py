# **** Lesson 10 : Files ****
# File Objects, Opening using default method [open()]
f = open('test.txt', 'r')
f.name
f.mode
f.close()
# *Note: When Using open(), we have to manually close the file by f.close()

# File Objects Opening using context manager, [with keyword]

with open('test.txt', 'r') as f:
    pass

# File Object is accessible outside the scope [However File remains closed]
f.closed

# Different Methods of reading files
# 1) read()                         This Method Serves well when files are short.
with open('test.txt', 'r') as f:
    file_contents = f.read()        # Returns a String

# 2) readlines()                    This Method Serves well when we need file contents in a list format
with open('test.txt') as f:
    file_contents = f.readlines()   # Returns a list

# 3) readline() and while loop      This Method is for reading 1 line at a time, more control can be provided
with open('test.txt', 'r') as f:
    file_contents = f.readline()    # Return 1 line, moves to the next line
    while file_contents:
        # print(file_contents, end='')
        file_contents = f.readline()

# 4) using only for loop            This is best for it's simplicity
with open('test.txt', 'r') as f:
    for line in f:                  # Simplest way!
        # print(line, end='')
        pass

# 5) read(character limit)          This provides more control to the amount of data being read
with open('test.txt', 'r') as f:
    file_contents = f.read(100)
    while file_contents:
        print(file_contents, end='*')
        file_contents = f.read(100)

# Other Properties
# f.tell()        # Tells how many character were read
# f.seek()        # Used to read the file from the beginning after each read

# Creating and Writing to Files
with open('test2.txt', 'w') as f:
    f.write('This is sample text')          # Creates and writes to file

with open('test2.txt', 'w') as f:
    f.write('This is a overwritten text')   # Overwrites The file

with open('test2.txt', 'a') as f:
    f.write('. This is appended text.')     # Appends to the file


# Demonstration of reading and writing, by creating and copying to test_copy from test
with open('test.txt', 'r') as main_file:
    with open('test_copy.txt', 'w') as copy_file:
        for line in main_file:
            copy_file.write(line)

# Demonstration of reading and writing, by creating and copying to cat_copy.jpg from cat.jpg
with open('cat.jpg', 'rb') as main_file:
    with open('cat_copy.jpg', 'wb') as copy_file:
        for line in main_file:
            copy_file.write(line)
