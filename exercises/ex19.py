# Function definition which takes two parameters
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# Direct print out with arguments passed
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# Passing an argument by a variable
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# passing argument using math
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# A combination of a variable and an integer as an argument
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
