# **** Lesson 8: Exploring Different Modules from Standard Library ****

import sys
import os
import datetime
import calendar

print(sys.path)
print(os.getcwd())
print(os.get_exec_path())

today = datetime.date.today()
print(today)
print(type(today))

print(calendar.isleap(2017))
print(calendar.isleap(2020))
