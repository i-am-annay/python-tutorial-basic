# ****Lesson 2 : Working with numbers in python****
num = 4
type(num)   # Returns <class 'int'>
num = 4.4
type(num)   # Return <class 'float'>

# ****Arithmatic Operators****
# Addition:         3 + 2
# Subtraction:      3 - 2
# Multiplication:   3 * 2
# Division:         3 / 2
# Floor Division:   3 // 2
# Exponent:         3 ** 2
# Modulus:          3 % 2

print(3 + 2)        # Prints 5
print(3 - 2)        # Prints 1
print(3 * 2)        # Prints 6
print(3 / 2)        # Prints 1.5
print(3 // 2)       # Prints 1
print(3 ** 2)       # Prints 9
print(3 % 2)        # Prints 1

# ****Incrementing Value****
num = 5
num = num + 1   # Increments by 1 and makes it 6
num += 1        # Increments by 1 and makes it 7 (Shorthand)
# num++         # Python does not support ++ or --
num += 10       # Increments by 10 and makes it 17
num *= 2        # Multiplies num with 2 and stores it in num
num /= 2        # Divides num by 2 and stores in in num and converts to float

# ****Built-In functions to work with numbers****
abs(-12)                    # Absolute Value
abs(12)                     # Absolute Value
round(4.75)                 # Rounds to the nearest decimal => 5
round(4.25)                 # Rounds to the nearest decimal => 4
round(4.75, 1)              # Rounds to the nearest decimal with 1 sf => 4.8
round(4.255, 2)             # Rounds to the nearest decimal with 2 sf => 4.25


# ****Comparison Operators****
# Equals:                   3 == 2
# Not Equals:               3 != 2
# Greater than:             3 > 2
# Less than:                3 < 2
# Greater Than or Equals:   3 >= 2
# Less Than or Equals:      3 <= 2

# ****Converting String to Integer****
num_1 = '100'
num_2 = '200'

num_1 = int(num_1)
num_2 = int(num_2)

sum = num_1 + num_2
print(sum)
