fruits = {"apple", "mango", "banana"}

# print(fruits[0])  # TypeError

print("apple" in fruits)
print("grapes" in fruits)

print("apple" not in fruits)
print("kiwi" not in fruits)

# =================================================
#   Practical use — checking if a user has access
# =================================================

allowed_users = {"Hussain", "Suleman", "Zaryab"}

user = input("Enter username: ")

if user in allowed_users:
    print("Access granted.")
else:
    print("Access denied!")
