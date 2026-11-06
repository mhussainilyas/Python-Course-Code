student = {
    "id": 595,
    "name": "Hussain",
    "age": 21,
}

print(f"Original = {student}")

# ====================
#   Updating Element
# ====================

# *** 1st Method ***

student["id"] = 126177

# *** 2nd Method ***

student.update(
    {
        "id": 126177,
        "name": "Muhammad Hussain",
    }
)

# ==================
#   Adding Element
# ==================

# *** 1st Method ***

student["gender"] = "Male"

# *** 2nd Method ***

student.update(
    {
        "city": "Lahore",
        "phone": 302_0133320,
        "state": "punjab",
    }
)


print(f"Modified = {student}")
