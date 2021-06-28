# **** Lesson 9 : OS module ****
import os
from datetime import date, datetime
# Printing Current Working Directory
os.getcwd()         # Outputs E:\Python\python_beginners_corey_schafer

# Switching Working Directory
path = 'D:\Study'
os.chdir(path)
os.getcwd()         # Outputs D:\Study

# Creating Directories
os.mkdir('Test_Directory')                  # Creates a directory
os.makedirs('Test_Directory1\Subfolder')    # + Subdirectories

print(os.listdir())                         # Shows all

# Removing Directories
os.rmdir('Test_Directory')                  # Deletes
os.removedirs('Test_Directory1\Subfolder')  # + Subfolders

print(os.listdir())                         # Shows all

# Getting file details
print(os.stat('test.txt'))                  # Provides All info
print(os.stat('test.txt').st_size)          # Size of file
print(os.stat('test.txt').st_mtime)         # Last Modified

# Printing Modification Time in date Format
modification_time = os.stat('test.txt').st_mtime
print(datetime.fromtimestamp(modification_time))

# Traversing the Directory Tree
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    # print('Current Path: ', dirpath)
    # print('Directories: ', dirnames)
    # print('Files: ', filenames)
    # print()
    pass

# Environment Variables
os.environ                  # All Varialbles
os.environ.get('HOMEPATH')  # Specified Variable
# Joining Path Names
file_path = os.path.join(os.environ.get('HOMEPATH'), 'text.txt')
print(file_path)

# os.path Module

# Getting basename, directoryname
os.path.basename('/tmp/test.txt')   # Returns File Name
os.path.dirname('/tmp/test.txt')    # Returns Directory Name
os.path.split('/tmp/test.txt')      # Splits File and Directory in Tuple

# *Note Here: '\' and '/' can be used within path names

# Checking for Valid Directories and files
os.path.isdir('/tmp/test.txt')      # Returs True/False if directory
os.path.isfile('/tmp/test.txt')     # Returs True/False if file
os.path.splitext('/tmp/test.txt')   # Returs Path Root and Extension in Tuple
