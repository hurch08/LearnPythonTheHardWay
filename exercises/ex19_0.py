def my_age(now, later):
    print(f"My age now is {now} years old")
    print(f"My later age will be {later} years old")
    print(f"That's all the information I can give you")

print("Arguments are passed directly")
my_age(12, 14)


print("Hey, let me try using a variable to tell my age")
now_age = 15
later_age = 17
my_age(now_age, later_age)

print("Great!, finally let me do some math")
my_age(12+9, 13+10)

print("Guess what!, I've almost exhausted my options. But let me try using a variable and some math together")
my_age(now_age + 1, later_age + 1)

print("Thank you all for your time")

# taking user inputs
now = int(input("Please enter your now age: "))
later = int(input("Please enter yourlater age: "))
print(f"Your now age is {now} years and your later age is {later} years old")
