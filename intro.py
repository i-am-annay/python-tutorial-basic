# ****Lesson 11: Automate Parsing and Renaming of Multiple Files****
import os

os.chdir("./Files")
for file in os.listdir():
    file_name, file_extension = os.path.splitext(file)
    file_first, file_middle, file_last = file_name.split('-')
    file_first = file_first.strip()
    file_middle = file_middle.strip()
    file_last = file_last.strip()[1:].zfill(2)

    new_name = f'{file_last}-{file_first}{file_extension}'
    os.rename(file, new_name)

# Earth - Our Solar System -  # 4.txt
# Jupyter - Our Solar System -  # 6.txt
# Mars - Our Solar System -  # 5.txt
# Mercury - Our Solar System -  # 2.txt
# Neptune - Our Solar System -  # 8.txt
# Pluto - Our Solar System -  # 10.txt
# Saturn - Our Solar System -  # 7.txt
# The Sun - Our Solar System -  # 1.txt
# Uranus - Our Solar System -  # 9.txt
