"""
Q7: Take a number as input. Print whether it is positive, negative, or zero.
"""

# num = int(input("Enter number: "))

# if num > 0:
#     print(f"{num} is positive")
# elif num < 0:
#     print(f"{num} is negative")
# else:
#     print(f"{num} is zero")

"""
Q8: Take two numbers as input. Print the greater of the two. If they are
equal, print "Both are equal."
"""

# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))

# if num1 > num2:
#     print(f"{num1} is greater")
# elif num2 > num1:
#     print(f"{num2} is greater")
# else:
#     print("Both are equal.")

"""
Q9: Take a student's marks as input. Print their grade based on this scale:
90 and above → A
75 to 89 → B
60 to 74 → C
40 to 59 → D
Below 40 → F
"""

# total_marks = int(input("Enter your marks: "))

# if total_marks >= 90 and total_marks <= 100:
#     print("Grade: A")
# elif total_marks >= 75 and total_marks < 90:
#     print("Grade: B")
# elif total_marks >= 60 and total_marks < 75:
#     print("Grade: C")
# elif total_marks >= 40 and total_marks < 60:
#     print("Grade: D")
# elif total_marks >= 0 and total_marks < 40:
#     print("Grade: F")
# else:
#     print("Invalid marks!")

# print("Done")

"""
Q10: Take a year as input. Check if it is a leap year. A year is a leap
year if it is divisible by 4, but not by 100, unless it is also
divisible by 400.
"""

# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap year.")
# else:
#     print("Not a leap year!")

"""
Q11: Take a person's age and whether they have a valid ID (True/False) as input. They
can enter a venue only if they are 18 or older AND have a valid ID. Print the
appropriate message
"""

# age = int(input("Enter your age: "))
# valid_id = input("Has valid ID: ").lower() == "true"

# if age >= 18:
#     print("Age requirement met.")
#     if valid_id == True:
#         print("You can enter a venue.")
#     else:
#         print("Valid ID is required!")
# else:
#     print("You are too young!")

"""
Q12: Take three numbers as input. Print the largest of the three without using any
built-in function.
"""

# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# num3 = int(input("Enter 3rd number: "))

# if num1 >= num2 and num1 >= num3:
#     print(f"{num1} is greater")
# elif num2 >= num1 and num2 >= num3:
#     print(f"{num2} is greater")
# else:
#     print(f"{num3} is greater")

"""
Q13: Take a number as input. Using the ternary operator, 
print "Even" or "Odd" in a single line.
"""

# num = int(input("Enter a number: "))
# result = "Even" if num % 2 == 0 else "Odd"
# print(f"{num} is {result}")

"""
Q14: A shop gives discounts based on purchase amount:
Above 5000 → 20% discount
Above 2000 → 10% discount
Above 1000 → 5% discount
1000 or below → no discount
"""

# purchase_amount = int(input("Enter your purchased amount: "))

# if purchase_amount > 5000:
#     discounted_amount = purchase_amount * (20 / 100)
#     final_amount = purchase_amount - discounted_amount
#     print(f"20% discount applied: {discounted_amount}")
#     print(f"Final amount: {final_amount}")
# elif purchase_amount > 2000:
#     discounted_amount = purchase_amount * (10 / 100)
#     final_amount = purchase_amount - discounted_amount
#     print(f"10% discount applied: {discounted_amount}")
#     print(f"Final amount: {final_amount}")
# elif purchase_amount > 1000:
#     discounted_amount = purchase_amount * (5 / 100)
#     final_amount = purchase_amount - discounted_amount
#     print(f"5% discount applied: {discounted_amount}")
#     print(f"Final amount: {final_amount}")
# elif purchase_amount >= 0:
#     print("0% discount applied: 0")
#     print(f"Final amount: {purchase_amount}")
# else:
#     print("Invalid purchase amount!")