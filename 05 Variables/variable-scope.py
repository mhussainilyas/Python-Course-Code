# ==========================
#   Global Scope Variables
# ==========================

x = 10

print(x)

def myFunc():
    print(x)

myFunc()

# =========================
#   Local Scope Variables
# =========================

def greet():
    word = "Hye!"
    print(word)

greet();

# print(word) # Error

# ====================
#   "global" keyword
# ====================

x = 10

def xyz():
    global y, z
    y = 20
    z = 30
    print(x, y, z)

xyz()

print(x, y, z)