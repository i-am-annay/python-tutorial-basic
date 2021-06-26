
print("Imported my_modules...")

test1 = 'Test String 1'
test2 = 'Test String 2'


def find_index(to_search, target):
    '''Find the index of a value in a sequence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1
