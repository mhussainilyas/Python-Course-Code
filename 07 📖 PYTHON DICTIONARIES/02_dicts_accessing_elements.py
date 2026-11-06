user_info = {
    "id": 595,
    "name": "Hussain",
    "age": 21,
    "is_student": True,
    "hobbies": ["reading", "sleeping", "coding"],
}

# ============================
#   Using Square Brackets []
# ============================

print(user_info["name"])
print(user_info["hobbies"])

# *** When we accessing KEY which is NOT EXISTS ***

print(user_info["department"])  # KeyError

# ==========================
#   Using the get() Method
# ==========================

print(user_info.get("id"))
print(user_info.get("name"))

# *** When we accessing KEY which is NOT EXISTS ***

print(user_info.get("department"))  # by default is NONE
print(user_info.get("department", -1))
print(user_info.get("department", False))

# =======================
#   Real World Scenario
# =======================

marks = {
    "math": 94,
    "urdu": 76,
    "english": 82,
    "computer": 71,
    "physics": 82,
}

user_subject = input("Enter your subject: ")
result = marks.get(user_subject)

if result is None:
    print(f"{user_subject} not found!")
else:
    print(f"{user_subject} = {result}")
