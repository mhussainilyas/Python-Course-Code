"""
Q44. Write a lambda function that takes a number and returns its cube. Store
it in a variable and call it
"""

# find_cube = lambda num: num ** 3
# print(f"The cube of 3 is = {find_cube(3)}")

"""
Q45. Write a lambda function that takes a number and returns
"Positive", or "Negative".
"""

# find_sign = lambda num: "Positive" if num >= 0 else "Negative"
# print(f"The number -5 is = {find_sign(-5)}")
# print(f"The number 10 is = {find_sign(10)}")

"""
Q46. Write a function fizzbuzz(n) that takes a single number and prints
"Fizz" if it's divisible by 3, 
"Buzz" if it's divisible by 5, 
"FizzBuzz" if it's divisible by both, 
otherwise print the number itself.
"""

# def fizzbuzz(n):
#     if n % 3 == 0 and n % 5 == 0:
#         print("FizzBuzz")
#     elif n % 3 == 0:
#         print("Fizz")
#     elif n % 5 == 0:
#         print("Buzz")
#     else:
#         print(n)

# fizzbuzz(9)
# fizzbuzz(20)
# fizzbuzz(15)
# fizzbuzz(7)

"""
Q47. Write a function power(base, exp) that returns base raised to exp using a
loop - no ** operator or pow() allowed.
"""

# def power(base, exp):
#     answer = 1
#     for _ in range(1, exp + 1, 1):
#         answer *= base
#     return answer

# result = power(2, 5)
# print(f"2 raised to the power of 5 is = {result}")

"""
Q48. Write a function tax_calculator(income) that takes annual income and returns
the tax amount based on these slabs:
Up to 2,50,000 → No tax
2,50,001 to 5,00,000 → 5%
5,00,001 to 10,00,000 → 20%
Above 10,00,000 → 30%
"""

# def tax_calculator(income):
#     if income <= 250000:
#         return 0
#     elif income <= 500000:
#         return (income - 250000) * 0.05
#     elif income <= 1000000:
#         return (250000 * 0.05) + ((income - 500000) * 0.20)
#     else:
#         return (250000 * 0.05) + (500000 * 0.20) + ((income - 1000000) * 0.30)


# tax_amount = tax_calculator(1200000)
# print(f"Tax amount = Rs. {tax_amount:.2f}")