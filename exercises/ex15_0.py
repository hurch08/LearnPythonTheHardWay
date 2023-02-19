# Modified to reduce the code

from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:\n")
print(txt.read())

print("Type the filename again:\n")

txt_again = open(input("::: "))

print("\n",txt_again.read())
