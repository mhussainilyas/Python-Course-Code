student = {
    "id": 595,
    "name": "Hussain",
    "age": 21,
    "gender": "Male",
    "city": "Lahore",
}

# ==================
#   "in" operators
# ==================

print("name" in student)
print("city" in student)
print(21 in student)  # False

# =====================
#   "not in" operator
# =====================

print("name" not in student)
print(21 not in student)

# =======================
#   Real world scenario
# =======================

data = {
    "id": 595,
    "name": "HSN",
    "nickname": "Gulu",
    "education": "Bachelor",
    "city": "Lahore",
    "is_student": True,
}

user_key = input("Enter your key: ")

if user_key in data:
    print(f"{user_key} = {data[user_key]}")
else:
    print(f"{user_key} not found!")
