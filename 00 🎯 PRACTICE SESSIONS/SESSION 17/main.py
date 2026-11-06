"""
Q79. Create a dictionary for a student, including keys like name, age,
city, and marks (as a list of scores). Print each piece of
information using its key.
"""

# student = {
#     "name": "Hussain",
#     "age": 21,
#     "city": "Lahore",
#     "marks": [48, 76, 87, 72],
# }

# for key in student:
#     print(f"{key} = {student[key]}")

"""
Q80. Define a dictionary with five subjects and their respective marks.
Utilize the get() method to try accessing a subject that is not in the
dictionary, ensuring it prints "Not Available" as a default.
"""

# marks = {
#     "urdu": 76,
#     "english": 82,
#     "computer": 71,
#     "physics": 82,
#     "math": 87,
# }

# result = marks.get("history", "Not Available")

# print(result)

"""
Q81. Construct a dictionary containing four product names and their
prices. Prompt the user to enter a product name. Use the in
keyword to check if it exists; if so, display its price. Otherwise,
inform the user "Product not found."
"""

# products = {
#     "laptop": 57_000,
#     "computer": 120_000,
#     "tablet": 67_000,
#     "mobile": 31_000,
# }

# user_product = input("Enter your product name: ")

# if user_product in products:
#     print(f"{user_product} price is = {products[user_product]}")
# else:
#     print(f"{user_product} not found!")

"""
Q82. Create a dictionary mapping five countries to their capital cities. Iterate
through this dictionary using the items() method and print each pair in
the format: Country → Capital.
"""

# countries = {
#     "Pakistan": "Islamabad",
#     "Australia": "Canberra",
#     "India": "New Delhi",
#     "England": "London",
#     "China": "Beijing",
# }

# print("--- Top 5 countries's capitals---")

# for country, capital in countries.items():
#     print(f"{country} → {capital}")

"""
Q83. Given a dictionary of marks for different subjects, loop over its values()
to calculate and print the total marks and the average mark obtained.
"""

# marks = {
#     "urdu": 76,
#     "english": 82,
#     "computer": 71,
#     "physics": 82,
#     "math": 87,
# }

# total = 0
# for mark in marks.values():
#     total += mark

# n = len(marks)
# average = total // n

# print(f"total marks = {total}")
# print(f"average marks = {average:.2f}")

"""
Q84. Populate a dictionary with six student names and their corresponding
marks. Loop through it and print the names of all students who achieved
a score above 75.
"""

# marks_result = {
#     "Hussain": 87,
#     "Suleman": 92,
#     "Zaryab": 89,
#     "Mudassir": 71,
#     "Hamid": 64,
#     "Huzaifa": 78,
# }

# for name, mark in marks_result.items():
#     if mark > 75:
#         print(f"{name}'s marks = {mark}")

"""
Q85. Write a Python function named merge_dicts(d1, d2) that accepts two
dictionaries (d1 and d2) as arguments and returns a new dictionary formed 
by merging them using the update() method. Ensure d1 remains unchanged.
"""


# def merge_dicts(d1, d2):
#     new_dict = {}
#     new_dict.update(d1)
#     new_dict.update(d2)
#     return new_dict


# dict_1 = {"a": 1, "b": 2}
# dict_2 = {"c": 3, "d": 4}

# new_dict = merge_dicts(dict_1, dict_2)

# print(f"Merged dict = {new_dict}")
