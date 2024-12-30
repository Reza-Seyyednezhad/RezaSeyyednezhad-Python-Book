# Condition Statement

# First Syntax (Only if)
"""
if condition:
    statement
"""

x = 25
# if x%2 == 1:
#     print(f"x:{x} is Odd number")

# print("----------------")

name = "Reza"
# if name == "ali":
#     print("Hello Ali")



# Second Syntax (if/else)
"""
if condition:
    statement
else:
    statement
"""

random_number = 1254
# if random_number%2 == 0:
#     print(f"{random_number} is Even number.")
# else:
#     print(f"{random_number} is Odd number.")
    
# print(" ------------------------------ ")
user_score = 5
# if user score grater than 10, user pass else Reject
# if user_score > 10:
#     print("Pass.")
# else:
#     print("Reject.")


# Third Syntax (if/elif/else) 
# Two Condition

user_score = 17

# if user_score >= 17:
#     print("Good Job.")
# elif 10 < user_score < 17:
#     print("Not Bad.")
# else:
#     print("It's Bad.")


# Third Syntax (if/elif/else) 
# Grater than Two Condition

user_color = "yellow"
# if user_color == "green":
#     print("First try: User color is green.")
# elif user_color == "red":
#     print("Second try: User color is red.")
# elif user_color == "black":
#     print("Third try: User color is black.")
# elif user_color == "white":
#     print("Fourth try: User color is white.")
# elif user_color == "yellow":
#     print("Fifth try: User color is yellow.")
# elif user_color == "blue":
#     print("Last try: User color is blue.")
# else:
#     print("Oh no, I can't guess color! :(")




# Conditions
a = 45
b = 13
# if a == b:
#     print("a and b are equal.")
    
# if a != b:
#     print("a and b are NOT equal.")

# if a > b:
#     print("a is grather than b.")

# if a >= b:
#     print("a is greater than or equal to b.")

# if a < b:
#     print("a is less than b.")

# if a <= b:
#     print("a is less than or equal to b.")


# And/Or in Condition Statement
name = "Reza"
age = 23

# if name == "Reza" and age == 24:
#     print("By And")
#     print(f"name = 'Reza':{name == "Reza"}")
#     print("AND")
#     print(f"age = 24: {age == 24}")
#     print(f"Result is {name == "Reza" and age == 24}")
    
# if name == "Reza" or age == 24:
#     print("By Or")
#     print(f"name = 'Reza':{name == "Reza"}")
#     print("OR")
#     print(f"age = 24: {age == 24}")
#     print(f"Result is {name == "Reza" or age == 24}")
    
    
# in keyword in condition statement
colors_list = ["red", "green", "blue", "black", "white"]

# if "yellow" in colors_list:
#     print("yellow is exist.")
# else:
#     print("yellow is NOT exist.")

# print("-----------------------")

# if 'blue' in colors_list:
#     print("blue is exist.")
# else:
#     print("blue is NOT exist.")


# not keyword in condition statement
colors_list = ["red", "green", "yellow", "orange", "white"]

# if "yellow" not in colors_list:
#     print("yellow is NOT exist.")
# else:
#     print("yellow is exist.")

# print("-----------------------")

# if 'blue' not in colors_list:
#     print("blue is NOT exist.")
# else:
#     print("blue is exist.")


# Nested if
# Buy Car
user_age = 24
user_certificate = True
if user_age >= 18:
    if user_certificate == True:
        print("You Can Buy Car. :)")
    else:
        print("You Don't Have Certificate. So You Can't Buy Car. :(")
else:
    print("Under legal age! :(")