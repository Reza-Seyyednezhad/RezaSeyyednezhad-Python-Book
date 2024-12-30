# Errors and Errors Handling

# Types of Errors
    # Syntax Errors
    # Runtime Errors
    # Logical Errors



# Types of Errors
    # Syntax Errors
    
# print("Hello World"


# Errors and Errors Handling

# Types of Errors
    # Syntax Errors
    # Runtime Errors
    # Logical Errors

# Runtime Errors

# print(100/0)

# my_list = [1, 2, 3]
# print(my_list[5])


# Errors and Errors Handling

# Types of Errors
    # Syntax Errors
    # Runtime Errors
    # Logical Errors

# Logical Errors
# def average(a, b):
#     return a + b / 2
#     # به صورت زیر محاسبه خواهد کرد
#     # a + (b/2)
# print(f"First Ans: {average(a=14,b=12)}")

# Solve Problem
# def average(a, b):
#     return (a + b) / 2
#     # به صورت زیر محاسبه خواهد کرد
#     # (a + b) / 2
# print(f"Second Ans: {average(a=14,b=12)}")


# Other Errors
    # TypeErrors

# def Sum_Operation(a, b):
#     return f"Sum of a , b: {a + b}"

# print(Sum_Operation("12", 4))


# Other Errors
    # ValueErrors

# def Value_Error_Example(a):
#     return f"{int(a)}"

# print(Value_Error_Example("Hello World!"))


# Other Errors
    # NameErrors

# هیچ متغیری یا تابعی تعریف نکردیم
# print(f"value of x is {x}")


# Other Errors
    # KeyErrors
# mydict = {
#     "firstName": "Reza",
#     "age": 23
# }
# # Available Key
# print(f"First Name:{mydict["firstName"]}")

# # Not Available Key
# print(f"Last Name:{mydict["lastName"]}")



# Other Errors
    # ImportErrors

# import nonexistent_module

# print(help(nonexistent_module))


# Errors Handling
    # Try/Except
    # Try/Except/Else/Finally

# Try/Except
"""
try:
    # کدی که ممکن است خطا تولید کند
except ErrorType:
    # کدی که در صورت رخ دادن خطا اجرا می‌شود

"""


# Errors Handling
    # Try/Except
# try:
#     result = 265 / 0
# except ZeroDivisionError:
#     print("Division by zero is not possible.")

# Errors Handling
    # Try/Except
# Many Except Section
# try:
#     num = int(input("Enter a number:"))
#     result = 10 / num
# except ValueError:
#     print("Please Enter Number Not Integer!")
# except ZeroDivisionError:
#     print("Division by zero is not possible!")

# Errors Handling
    # Try/Except
# If Error is not clear:
# try:
#     num = int("hello")
# except:
#     print("An unspecified error has occurred.")


# Errors Handling
    # Try/Except/Else/Finally

# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ZeroDivisionError:
#     print("Division by zero is not possible!")
# except ValueError:
#     print("The Input is invalid!")
# else:
#     print("Result:", result)
# finally:
#     print("End of the process.")



