def greet(name, age):
    print(f"Hye! {name}")
    print(f"Your age is {age}")

greet("Hussain", 21)

# ==============
#   Example 01
# ==============

def sum_of_numbers(a, b, c):
    ans = a + b + c
    print(f"sum is = {ans}")

sum_of_numbers(1, 2, 3)

# ==============
#   Example 02
# ==============

def user_info(name, age, gender):
    print(f"Hye! {name}")
    print(f"Your age is {age}")
    print(f"You are {gender}")

user_name = input("Enter your name: ")
user_gender = input("Enter your gender: ")
user_age = int(input("Enter your age: "))

user_info(user_name, user_age, user_gender)

