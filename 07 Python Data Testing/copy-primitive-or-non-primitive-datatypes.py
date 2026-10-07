# ================================
#   Non Primitive Data Type Copy
# ================================

userList1 = ["Hussain", "Suleman"]

userList2 = userList1

print(hex(id(userList1)))
print(hex(id(userList2)))

userList1[0] = "Zaryab"

print(userList1)
print(userList2)

# ============================
#   Primitive Data Type Copy
# ============================

a = 10
b = a

print(hex(id(a)))
print(hex(id(b)))

b = 20

print(f"a = {a} and b = {b}")

print(hex(id(a)))
print(hex(id(b)))