# Scope Section

# Local Scope
# def my_function():
#     x = 45  # Local Scope
#     # در داخل تابع می‌توان ایکس را فراخوانی کرد
#     print(f"function Result is {x}")

# my_function()
# # اگر ایکس را در خارج از تابع فراخوانی کنیم، خطا خواهد داد
# print(x)  


# Scope Section
# Enclosing
# def outer():
#     y = 20  # Enclosing Scope
#     def inner():
#         print(y)  # دسترسی به متغیر Enclosing
#     inner()
# outer()


# Scope Section
# Global Scope

x = 30  # Global Scope

# def my_function():
#     print(f"function Result: {x}")  # در داخل تابع  می‌توان به ایکس دسترسی داشت
# my_function()

# print(f"Global Scope: {x}") # در خارج از تابع می‌توان به ایکس دسترسی داشت



# Global Scope and global keyword
# Convert local Scope to global scope

# x = 10  # متغیر سراسری
# def my_function():
#     global x
#     x = 20  # تغییر متغیر سراسری
#     print(f"In the Function: {x}")
# my_function()
# print(f"Out the Function: {x}")  # مقدار تغییر کرده است


# Local Scope and nonlocal keyword
def outer():
    x = 10  # متغیر Enclosing

    def inner():
        nonlocal x
        x = 20  # تغییر مقدار متغیر Enclosing
        print("Inner:", x)

    inner()
    print("Outer:", x)

outer()

