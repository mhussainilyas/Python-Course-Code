student = {
    "name": "Hussain",
    "age": 21,
    "city": "Lahore",
}

# =====================
#   Looping over keys
# =====================

print("--- Looping over Keys ---")

for key in student:
    print(key)

# ================================
#   Explicitly looping over keys
# ================================

for key in student.keys():
    print(key)

# =======================
#   Looping over values
# =======================

print("--- Looping over Values ---")

for value in student.values():
    print(value)

# ==============================================
#   Looping over key-value pairs using items()
# ==============================================

print("--- Looping with items() ---")

for key, value in student.items():
    print(f"{key} = {value}")

# ==========================================
#   Practical use — filter based on values
# ==========================================

marks = {
    "math": 85,
    "science": 92,
    "english": 60,
    "hindi": 45,
}

for subject, score in marks.items():
    if score >= 80:
        print(f"{subject}: Excellent")
    elif score >= 60:
        print(f"{subject}: Good")
    else:
        print(f"{subject}: Need Improvement")

# *** Counting values that match a condition ***
# *** (using .values() directly here) ***

passed_subject = 0
for score in marks.values():
    if score >= 50:
        passed_subject += 1

print(f"Passed subjects = {passed_subject}")
