# This imports the argument variable from the sys module
from sys import argv

# unpacking the argument variable to the two variables below
script, filename = argv

# opening the file before reading takes place
txt = open(filename)

# File reading has started
print(f"Here's your file {filename}:")
print(txt.read())
txt.close()

# Accepting user filename from the user
print("Type the filename again:")
file_again = input("> ")

# opening the file provided by the user
txt_again = open(file_again)

# printing the file after reading it
print(txt_again.read())
txt_again.close()
