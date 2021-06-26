# **** Lesson 7: Functions ****

# The most basic function body
def fun():
    pass

# print(fun)        Outputs the address of the function in memory
# print(fun())      Outputs 'None'

# Note: 1 function may have multiple definitions, the latest one overrides all previous definition.

# Defining funtions


def hello():                  # Initial Definition
    return 'hello'


# print(hello())              # Outputs 'hello'


def hello():                  # Overriden Definition
    return "Hello There!"


# print(hello())              # Outputs 'Hello There!'

# Required Positional Arguments [Mandatory]


def hello(greeting):
    return '{}, there'.format(greeting)


# print(hello('Hello'))       # Outputs 'Hello, there'
# print(hello('Hi'))          # Outputs 'Hi, there'
# print(hello('Hey'))         # Outputs 'Hey, there'

# Key Word Arguments [Optional]

def hello(greeting, name='Jhon'):
    return '{}, {}'.format(greeting, name)


# print(hello('Hello'))               # Outputs 'Hello, Jhon'
# print(hello('Hello', 'Jane'))       # Outputs 'Hello, Jane'
# print(hello('Hello', 'Mary'))       # Outputs 'Hello, Mary'
# print(hello('Hello', name='Mary'))  # Outputs 'Hello, Mary'


# Multiple Arguments
def student(*args):
    print(args)


# student('Bob', 'Sam', 'Jhon', 'Mario')


def student(*args, **kwargs):
    print(args)         # args = Tuple
    print(kwargs)       # kwargs = Dictionary


# student('Bob', 'Sam', age=23, height=5.5)

# Unzipping in Function Invocation
name = ['Bob', 'Sam']
properties = {
    'age': 23,
    'height': 5.5
}

# student(name, properties)       # Without Unzipping
# student(*name, **properties)    # With Unzipping

# Complex Unzipping (*Practice This more*)
student(*name, *properties, name, **properties)
