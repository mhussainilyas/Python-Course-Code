marks = {
    "math": 87,
    "urdu": 76,
    "english": 82,
    "computer": 71,
}

print(marks)
print(type(marks))
print(f"length = {len(marks)}")

# =========================
#   Mixed Example of Dict
# =========================

user_info = {
    "id": 595,
    "name": "Hussain",
    "age": 21,
    "is_student": True,
    "hobbies": ["reading", "sleeping", "coding"],
}

print(user_info)
print(f"length = {len(user_info)}")

# ===============================
#   Dictionary with number keys
# ===============================

roll_to_name = {
    101: "Hussain",
    102: "Suleman",
    103: "Zaryab",
}

print(roll_to_name)
print(f"length = {len(roll_to_name)}")


# =========================
#   Immutable key Example
# =========================

data_sets = {
    "name": "Hussain",
    "department": "BSCS",
    "uni_roll_no": 126177,
    # ["c1", "c2"]: True, # TypeError
    ("c1", "c2"): True,
}

print(data_sets)
print(data_sets[("c1", "c2")])  # True
