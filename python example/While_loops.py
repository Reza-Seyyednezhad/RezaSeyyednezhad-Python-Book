# While loops in Python Programming

# 1
# count = 1
# while count <= 5:
#     # print(count)
#     count += 1


# 2
# countdown = 10
# while countdown > 0:
    # print(countdown)
    # countdown -= 1
# print("End of Counting!")


# 3
# number = int(input("Enter a number: "))
# factorial = 1
# count = 1
# while count <= number:
#     factorial *= count
#     count += 1
# print(f"Factorial of {number} is: {factorial}")


# ** Else Statement in While loop **

# count = 1
# while count <= 5:
#     print(count)
#     count += 1
# else:
#     print("End of the Loop!")


# ** Break in While Loop **

# number = 0
# while True:  
#     number += 1  
#     print(f"Checking number: {number}")
#     if number == 5:  
#         print("Number 5 found, exiting the loop.")
#         break  
# print("Loop ended.")


# ** Continue in While Loop **

number = 0
while number < 10:
    number += 1  
    if number % 3 == 0: 
        continue  
    print(f"Checking number: {number}")
