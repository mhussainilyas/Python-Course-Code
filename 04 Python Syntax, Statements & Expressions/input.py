name = input("Enter your name: ")

print("Hye!", name)

# =====================
#    Important Point
# =====================
# The input() function always returns the entered value as a string (str), even if the user enters a number

num1 = input("Enter 1st number: ")
num2 = input("Enter 2nd number: ")

result = int(num1) + int(num2)

print(f"sum of {num1} and {num2} = {result}")