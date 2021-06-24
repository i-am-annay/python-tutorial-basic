# ****String****
message1 = 'Hello World'        # String in Single Quotes
message2 = "Hello World"        # String in Double Quotes

message3_1 = 'Annay\'s Plan'    # String of Single Quotes containing Single Quotes
message3_2 = "Annay's Plan"     # String of Double Quotes containing Single Quotes

message4_1 = '"Double" Trouble'  # String of Single Quotes containting Single Quotes
# String of Double Quotes containing Double Quotes
message4_2 = "\"Double\" Trouble"

# Notes: Backslash (\) is used as an escape Sequence

# ****Multiline String****
paragraph = """
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
    when an unknown printer took a galley of type and scrambled it to make a type
    specimen book. It has survived not only five centuries, but also the leap into 
    electronic typesetting, remaining essentially unchanged. It was popularised in the 
    1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
    and more recently with desktop publishing software like Aldus PageMaker including versions 
    of Lorem Ipsum.
"""

# ****Slicing Strings****
name = "Annay Paul"
name[0]     # Returns the character on the 0th index
name[1]     # Returns the character on the 1st index
name[-1]    # Returns the character on the last index
name[:4]    # Returns the set of characters from the beginning up to the 4th index but not including the 4th index
name[2:]    # Returns the set of characters from the 2nd index till the end
name[2:4]   # Returns the set of characters from the 2nd index till the 4th index but not including the 4th index

# ****Getting Length of Strings****
len(name)   # len() -> built in function that returns the number of characters in the string

# ****Converting into lower case****
name_lower = name.lower()    # Returns a new string with all characters in lower case

# ****Converting into upper case****
name_upper = name.upper()    # Returns a new string with all characters in upper case

# ****Counting how many times a character/substring appears****
name.count('n')  # Returns the number of 'n' in the name 'Annay Paul'
name.count('au')  # Returns the number of 'au' in the name 'Annay Paul'

# ****Searching the index of a character/substring ****
name.find('n')   # Returns the index of the 1st occurence of the letter 'n'
name.find('au')  # Returns the index of the 1st occurence of the substring 'au'
name.find('x')   # Returns -1 if not found

# ****Replacing a section of a string****
message1_new = message1.replace('World', 'Universe')

# ****String concatation****
greeting = 'Hello'
message = greeting + ', ' + name    # Returns 'Hello, Annay Paul'

# ****Fomratted Strings****
message = '{}, {}'.format(greeting, name)   # {} act as place holders
message = f'{greeting}, {name}'  # f-strings, effective for python 3.6>

# ****Finding out documentation****
print(dir(str))            # Lists all attributes and methods
print(help(str))           # Lists all attributes and methods with documentation
print(help(str.lower))     # Provides documentation of the specific attribute
