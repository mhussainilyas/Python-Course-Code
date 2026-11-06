students = {
    "101": {"name": "Hussain", "age": 21, "city": "Lahore"},
    "102": {"name": "Suleman", "age": 22, "city": "Multan"},
    "103": {"name": "Zaryab", "age": 20, "city": "Karachi"},
}

# ============================================
#   Accessing nested values — chain the keys
# ============================================

print(students["101"])
print(students["101"]["name"])
print(students["102"]["city"])

# ========================
#   Adding a new student
# ========================

students["104"] = {"name": "Ali", "age": 19, "city": "Narowal"}

# ===========================
#   Updating a nested value
# ===========================

students["104"]["age"] = 20

# =======================================
#   Looping through a nested dictionary
# =======================================

for roll_no, detail in students.items():
    print(f"roll_no {roll_no}: {detail["name"]} from {detail["city"]}")

# print(students)
