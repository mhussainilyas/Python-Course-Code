student = {
    "name": "Hussain",
    "age": 21,
    "subjects": ["Math", "Computer", "English"],
    "marks": [87, 71, 82],
}

# ===============================================
#   Accessing list elements inside a dictionary
# ===============================================

print(student["subjects"])
print(student["subjects"][0])
print(student["marks"][1])

# ===================================================
#   Modifying a list directly within the dictionary
# ===================================================

student["subjects"].append("urdu")
student["marks"].append(76)

# =======================
#   Real-world scenario
# =======================

university = {
    "bscs": ["Hussain", "Ahsan", "Asad"],
    "bsit": ["Faizan", "Hamid", "Ali Raza", "Umar"],
    "bsai": ["Zaryab", "Suleman"],
}

for dept, students in university.items():
    print(f"{dept.upper()} — {len(students)} students")
    for std in students:
        print(f" - {std}")
