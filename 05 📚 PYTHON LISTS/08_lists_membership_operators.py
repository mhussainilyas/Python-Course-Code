fruits = ["apple", "banana", "cherry"]

# =============================
#   in - Check for Membership
# =============================

is_exists = "apple" in fruits
is_exists = "orange" in fruits
print(f"exists in fruit = {is_exists}")

# =====================================
#   not in - Check for Non-Membership
# =====================================

is_not_exists = "grapes" not in fruits
is_not_exists = "banana" not in fruits
print(f"not exists in fruit = {is_not_exists}")
