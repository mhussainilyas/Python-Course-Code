# =========================
#   Union (| or .union())
# =========================

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# ***  Using the | operator ***
result_1 = set_a | set_b

# *** Using the union() method ***
result_2 = set_a.union(set_b)

print(result_2)

# =======================================
#   Intersection (& or .intersection())
# =======================================

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# ***  Using the & operator ***
result_1 = set_a & set_b

# *** Using the intersection() method ***
result_2 = set_a.intersection(set_b)

print(result_2)

# ===========================================
#   Real-world Application: Student Records
# ===========================================

math_students = {"Ali", "Ahmad", "Shoaib", "Babar"}
science_students = {"Ahmad", "Shoaib", "Hussain"}

print("Students in BOTH Math and Science:")
print(math_students & science_students)

print("Students in EITHER Math OR Science:")
print(math_students | science_students)

