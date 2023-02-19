# Prompting and Passing

from sys import argv

script, fname, lname = argv
prompt = '> '

print(f"Hi {fname} {lname}, I'm the {script}.")
print("i'd like to ask you a few questions.")
print(f"Do you like me {fname} {lname}?")
likes = input(prompt)

print(f"Where do you live {fname} {lname}?")
lives = input(prompt)

print(f"What computer do you use {fname} {lname}?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
