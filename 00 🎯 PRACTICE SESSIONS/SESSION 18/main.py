"""
Q86. Create a dictionary of 6 subjects and their respective marks. Print the subject
with the highest marks and the one with the lowest, using max() and min()
functions alongside a lambda expression.
"""

# marks = {
#     "computer": 71,
#     "english": 82,
#     "urdu": 76,
#     "physics": 82,
#     "math": 87,
#     "islamiyat": 48,
# }

# highest = max(marks.items(), key=lambda x: x[1])
# lowest = min(marks.items(), key=lambda x: x[1])

# print(f"Maximum marks is {highest[1]} in {highest[0]}")
# print(f"Maximum marks is {lowest[1]} in {lowest[0]}")

"""
Q87. Create a nested dictionary containing details for 4 students, where each
student entry includes their name, age, and city. Write a loop to print the full
details of each student in a clear, readable format.
"""

# students = {
#     "101": {"name": "Hussain", "age": 21, "city": "Lahore"},
#     "102": {"name": "Shoaib", "age": 20, "city": "Faisalabad"},
#     "103": {"name": "Ali", "age": 20, "city": "Narowal"},
#     "104": {"name": "Ahmed", "age": 22, "city": "Karachi"},
# }

# for roll, std in students.items():
#     print(f"Roll No: {roll}")
#     for key, value in std.items():
#         print(f"{key.capitalize()} = {value}")
#     print()

"""
Q88. Design a dictionary where each key is a student's name and the
corresponding value is a list of their marks in 3 different subjects. Calculate
and print the total marks and average marks for each student.
"""

# students = {
#     "Hussain": [71, 82, 48],
#     "Suleman": [74, 86, 49],
#     "Zaryab": [68, 76, 46],
#     "Hamid": [54, 68, 30],
# }

# for name, marks in students.items():
#     total = sum(marks)
#     average = total // len(marks)
#     print(f"{name} has scored {total} marks with the average of {average:.2f}")

"""
Q89. Given a dictionary of subjects and their marks, sort it by marks in descending
order. Then, print only the top 3 subjects with the highest marks.
"""

# marks = {
#     "computer": 71,
#     "physics": 82,
#     "islamiyat": 48,
#     "mathematics": 87,
#     "english": 82,
#     "urdu": 76,
# }

# result = sorted(marks.items(), key=lambda x: x[1], reverse=True)
# top_result = dict(result[0:3])

# for sub, mark in top_result.items():
#     print(f"subject = {sub.capitalize()} and marks = {mark}")

"""
Q90. Using dictionary comprehension, create a new dictionary where keys are 
numbers from 1 to 10 (inclusive), and values are the cube of each number.
"""

# cubes = {i: i**3 for i in range(1, 11)}

# print(cubes)

"""
Q91. Given an existing dictionary of subjects and their respective marks, 
use dictionary comprehension to generate a new dictionary that includes
only the subjects where the student scored 40 or more (i.e., passed).
"""

# marks = {
#     "computer": 28,
#     "physics": 82,
#     "islamiyat": 48,
#     "mathematics": 87,
#     "english": 32,
#     "urdu": 76,
# }

# passed_subjects = {sub: mark for sub, mark in marks.items() if mark >= 40}

# for sub, mark in passed_subjects.items():
#     print(f"subject = {sub.capitalize()} and marks = {mark}")

"""
Q92. You have two separate lists: one containing subject names and 
another containing corresponding marks. Create a dictionary from these two
lists using dictionary comprehension, mapping each subject to its mark.
"""

# marks = [71, 82, 87, 76]
# subjects = ["computer", "physics", "math", "urdu"]

# result = {sub: mark for sub, mark in zip(subjects, marks)}

# print(result)
