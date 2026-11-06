"""
Q1: Take two numbers as input from the user. Print their sum, difference,
product, and remainder.
"""

# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# print(f"Sum = {num1 + num2}")
# print(f"Difference = {num1 - num2}")
# print(f"Product = {num1 * num2}")
# print(f"Remainder = {num1 % num2}")

"""
Q2: Take a number as input. Print whether it is even or odd using the %
operator and a comparison operator.
"""

# num = int(input("Enter number: "))
# print(f"{num} is even = {num % 2 == 0}")

"""
Q3: Take the user's age as input. Check and print whether they are eligible
to vote (age >= 18) and whether they are a senior citizen (age >= 60).
Print both results.
"""

# age = int(input("Enter your age: "))
# can_vote = age >= 18
# senior_citizen = age >= 60
# print(f"User can vote = {can_vote}")
# print(f"User is senior citizen = {senior_citizen}")

"""
Q4: A student scored marks in 3 subjects. Take all three as input,
calculate the total and average, and print both using an f-string.
"""

# subject1 = int(input("Enter marks if subject 1: "))
# subject2 = int(input("Enter marks if subject 2: "))
# subject3 = int(input("Enter marks if subject 3: "))
# total_marks = subject1 + subject2 + subject3
# average_marks = total_marks / 3
# print(f"Total marks is = {total_marks}")
# print(f"Average marks is = {average_marks:.2f}")

"""
Q5: Take a number as input. Print the result of that number raised to the
power of 3 using **. Also print what // 7 and % 7 give for the same number
"""

# num = int(input("Enter number: "))
# print(f"{num} raised to the power of 3 is = {num ** 3}")
# print(f"floor division of {num} with 7 is = {num // 7}")
# print(f"{num} modulus 7 is = {num % 7}")

"""
Q6: Take two numbers as input. Without using *, calculate and print their product
using += in a way that adds the first number to itself the
second number of times. (Think carefully.)
"""

# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))

# product = 0

# for i in range(num2):
#     product += num1

# print(f"Product of {num1} in {num2} times is = {product}")