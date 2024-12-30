# For Loops in Python

# 1
# for number in [1,2,3,4,5]:
#     print(number)


# Range in loops

# for i in range(5):
#     print(f"This number is: {i}")


# ** Else Statement in For loop **

# items = [2, 4, 6, 8]
# target = 5
# for item in items:
#     if item == target:
#         print("Not Found the Number!:(")
#         break
# else:
#     print("list index out of range!:(")


# Example 1: Student's Score

# grades = [18, 20, 17, 19, 15] # لیست نمرات دانشجو

# total = 0 # متغیر برای جمع نمرات

# for grade in grades: # حلقه‌ برای جمع کردن نمرات
#     total += grade
    
# average = total / len(grades) # محاسبه میانگین

# print("Avrage of Scores: ", average) # نمایش میانگین


# Example 2: Seprate Even an Odd numbers from a list
# main_numbers_list = [45, 2, 49, 17, 65, 98, 11, 83, 15, 32] # فهرست اعداد تصادفی

# even_numbers_list = [] #ایجاد فهرست برای افزودن اعداد زوج 
# odd_numbers_list = [] #ایجاد فهرست برای افزودن اعداد فرد 

# for i in main_numbers_list: #استفاده از حلقه برای پیمایش بر روی فهرست اعداد تصادفی
#     if i%2 == 0: # استفاده از دستورات شرطی برای یافتن اعداد زوج و فرد و جداسازی آن ها
#         even_numbers_list.append(i)
#     elif i%2 != 0:
#         odd_numbers_list.append(i)
#     else:
#         print("The number is not even or odd!")

# # چاپ کردن فهرست اعداد زوج و فرد به صورت جداگانه
# print(f"The Even numbers list is: {even_numbers_list}")
# print(f"The Odd numbers list is: {odd_numbers_list}")


# Example 3: Separate Character of String.

# string_example = "Apples"
# char_list = []

# for char in string_example:
#     char_list.append(char)
#     print(f"The character in this loop is: {char}")

# print(f"List of Characters: {char_list}")


# Example 4: Separate keys and values from a Dictionary.
# main_dict = {
#     "name": "Reza",
#     "age": 23,
#     "job": "Student",
#     "mobile": "09011111111",
#     "favorite color": "yellow"
# }
# keys_list = []
# values_list = []

# for key, value in main_dict.items():
#     keys_list.append(key)
#     values_list.append(value)

# print(f"The Keys of main_dict are: {keys_list}")
# print(f"The Values of main_dict are: {values_list}")


# Example 5: multiple of the numbers list

# numbers_list = [2, 7, 1, 3]  # فهرست نمونه‌ای از اعداد
# multiple = 1  # متغیر برای ذخیره حاصل‌ضرب، مقدار اولیه ۱
# for number in numbers_list:
#     print(f"This loop: {multiple} * {number}: {multiple*number}")
#     multiple *= number  # multipleضرب هر عنصر در متغیر 

# print("The multiple of the list is:", multiple)


# ** Nested Loops **

for i in range(1, 4):
    for j in range(1, 3):
        print(f"i: {i}, j: {j}")


