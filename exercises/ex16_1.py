# importing argument variable from the sys module
from sys import argv

# Unpacking the argument variables
script, filename = argv

# initial prompt for asking the user to make a decision
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# taking response from the user
input("?")

#printing a prompt to indicate the opening of a file
print("opening the file...")
target = open(filename, 'w')

#erasing the content of the file
#print("Truncating the file. Goodbye!")
#target.truncate()

# writing codes to be stored in the text files
print("Now I'm going to ask you for three lines")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(f"{line1} \n{line2} \n{line3} \n")

print("And finally, we close it.")

target.close()
