# Prompting and Passing
# Modified with a change of prompt variable

from sys import argv

script, user_name = argv
prompt = ':::: '

print(f"Hi {user_name}, I'm the {script}.")
print("i'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What computer do you use {user_name}?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
