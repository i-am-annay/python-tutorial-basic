# **** Lesson 6: Loops****
nums = [1, 2, 3, 4, 5]
# Basic Iterations
for num in nums:
    # print(num)
    pass

for i in range(10):
    # print(i)
    pass

for i in range(5, 10):
    # print(i)
    pass

# Note: range(start, end) -> Creates a range from start up to but not including end

# Break and Continue
for num in nums:
    if num == 3:
        break           # Breaks out of the loop for the condition
    # print(num)

for num in nums:
    if num == 3:
        continue        # Skips the iteration at the condition
    # print(num)

# ****Nested Loops****
numbers = [1, 2, 3, 4, 5]
word = 'hey'

for num in numbers:
    for letter in word:
        # print(num, letter)
        pass

# ****While Loops****
x = 1
while x <= 10:
    print(x)
    x += 1


y = 1
while True:
    print(y)
    if y == 10:
        break
    y += 1
