marks = {
    "science": 56,
    "math": 94,
    "computer": 71,
    "urdu": 76,
    "english": 82,
}

# ===================================================
#   update() — add or update multiple pairs at once
# ===================================================

marks.update({"Islamiyat": 48, "science": 68})

# ========================
#   get() — safer access
# ========================

print(marks.get("computer"))
print(marks.get("Biology", 0))

# ========================================
#   copy() — creates an independent copy
# ========================================

data = {"a": 1, "b": 2}

copy_data = data.copy()

copy_data.update({"c": 3})

print(f"original data = {data}")
print(f"copy data = {copy_data}")

# =======================================
#   keys() — returns a view of all keys
# =======================================

marks_keys = marks.keys()

for subject in marks_keys:
    print(f"{subject} marks = {marks[subject]}")

# ===========================================
#   values() — returns a view of all values
# ===========================================

marks_values = marks.values()

total = 0
for mark in marks_values:
    total += mark

print(f"total marks = {total}")


# ==============================================================
#    items() — returns a view of all key-value pairs as tuples
# ==============================================================

marks_items = marks.items()

# *** 1st Method ***

for subj_detail in marks_items:
    subject = subj_detail[0]
    obtained_marks = subj_detail[1]
    print(f"{subject} marks = {obtained_marks}")

# *** 2nd Method ***

for subject, mark in marks_items:
    print(f"{subject} marks = {mark}")
