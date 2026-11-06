# =================
#   Creating List
# =================

numbers = [100, 200, 300, 400, 500]
students = ["Hussain", "Suleman", "Zaryab"]
user_data = ["Hussain", 21, "Male", True, 3.47]

print(numbers, type(numbers))
print(students, type(students))
print(user_data, type(user_data))

# ===================
#   List Operations
# ===================

# ===== Repeating Lists with `*` =====
data_list_1 = [1, 2, 3, 4]
new_data_list_1 = data_list_1 * 4
print(f"Repeated List: {new_data_list_1}")

# ===== Concatenating Lists with `+` =====
data_list_1 = [1, 2, 3, 4]
data_list_2 = [5, 6, 7, 8]
new_data_list = data_list_1 + data_list_2
print(f"Concatenated List: {new_data_list}")

