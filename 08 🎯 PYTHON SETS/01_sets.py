# ==========================
#   Set with string values
# ==========================

fruits = {"apple", "mango", "banana"}

print(f"Fruits set: {fruits}")
print(type(fruits))

# ====================
#   Set with numbers
# ====================

nums = {1, 2, 3, 4, 5}

print(f"Numbers set: {nums}")
print(type(nums))

# =============================
#   Set with mixed data types
# =============================

mixed = {"Rahul", 21, True, 9.5}

print(f"Mixed set: {mixed}")
print(type(mixed))

# =================================================================
#   Creating a set from a list, automatically removing duplicates
# =================================================================

my_list = [1, 2, 3, 2, 1, 4, 5, 4]

unique = set(my_list)

print(f"Unique elements from list: {unique}") 
