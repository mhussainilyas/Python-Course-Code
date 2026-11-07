# ==========================
#   Set to List conversion
# ==========================

nums = {10, 20, 30, 20, 10, 40}
print(f"Set = {nums}")

nums_list = list(nums)
print(f"List = {nums_list}")

# ==========================
#   List to Set conversion
# ==========================

my_list = [54, 65, 43, 32, 32, 3, 43, 43, 43, 43]
print(f"List = {my_list}")

my_set = set(my_list)
print(f"Set = {my_set}")

# ===================
#   General Example
# ===================

my_list = [1, 2, 3, 2, 1]

my_set = set(my_list)  # Converts list to set: {1, 2, 3}

back_list = list(my_set)  # Converts set back to list: [1, 2, 3]

my_tuple = tuple(my_set)  # Converts set to tuple: (1, 2, 3)
