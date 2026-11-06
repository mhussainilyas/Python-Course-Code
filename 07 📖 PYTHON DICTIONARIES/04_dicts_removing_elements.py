student = {
    "id": 595,
    "name": "Hussain",
    "age": 21,
    "gender": "Male",
    "city": "Lahore",
}

print(f"Original = {student}")

# ============
#   pop(key)
# ============

deleted_element = student.pop("age")

print(f"Value of deleted element = {deleted_element}")

# ==================
#   clear() Method
# ==================

student.clear()

# =================
#   del Statement
# =================

del student  # It del the complete variable from memory
del student["id"]

print(f"Modified = {student}")
