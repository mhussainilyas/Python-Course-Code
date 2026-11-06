# ============================
#   Normal way — using a loop
# ============================

squares = {}

for i in range(1, 6, 1):
    squares[i] = i**2


# ======================================================
#   Dictionary comprehension — same result in one line
# ======================================================

squares = {i: i**3 for i in range(1, 6)}

# ====================
#   With a condition
# ====================

marks = {
    "math": 85,
    "science": 92,
    "english": 60,
    "hindi": 45,
}

top_marks = {sub: mark for sub, mark in marks.items() if mark > 80}

# ==================================
#   Creating a dict from two lists
# ==================================

subjects = ["computer", "physics", "math"]
marks = [71, 82, 87]

subject_marks = {sub: mark for sub, mark in zip(subjects, marks)}

print(subject_marks)
