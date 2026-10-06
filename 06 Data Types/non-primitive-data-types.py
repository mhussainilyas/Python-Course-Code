# ===========
#   1) List
# ===========
# ordered collection of items
# mutable (can be changed)
# allows duplicate values

shopping_cart = ["milk", "eggs", "rice", 'tea', "milk"]
print(shopping_cart)

shopping_cart[0] = "water"
shopping_cart[1] = "sugar"
print(shopping_cart)

mix_list = ["Hussain", 21, True, None]
print(mix_list)

# ============
#   2) Tuple
# ============
# ordered collection of items
# immutable (cannot be changed)
# allows duplicate values

co_ordinates = (24.923423, 67.234234)
print(co_ordinates)

months = ("January", "February", "March", "April")
print(months)

color = (255, 255, 255)
print(color)

# color[0] = 175 # Error - bcz Tuples are immutable

print(color[0])
print(color[1])
print(color[2])

# ==========
#   3) Set
# ==========
# unordered collection of items
# stores unique values
# mutable (can be changed)

users = {"Hussain", "Suleman", "Ali", "Hussain"}
print(users)

# print(users[0]) # Error - bcz set are unordered collection of items

users.add("Zaryab")
users.remove("Ali")

print(users)

# =================
#   4) Dictionary
# =================
# stores key-value pairs
# keys must be unique
# mutable (can be changed)

student = {
    "name": "Hussain",
    "age": 21,
    "city": "Lahore",
    "is_student": True
}

print(student)

student["name"] = "HSN"
student["city"] = "LHR"

print(student)
print(student["name"])
print(student["age"])