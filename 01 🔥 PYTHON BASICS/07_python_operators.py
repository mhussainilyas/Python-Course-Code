# ========================
#   Arithmetic Operators
# ========================

a = 5
b = 10

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(20 // 10) # floor division

print(2 ** 5) # exponent
print(81 ** 0.5) # find root (x ** 0.5)

print(24 % 10) # modulus

# ========================
#   Comparison Operators
# ========================

a = 20
b = 10

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# =====================
#   Logical Operators
# =====================

physics = 32
computer = 45

print(physics > 33 and computer > 33)
print(physics > 33 or computer > 33)
print(not physics > 33)

print(not(physics > 33) and not(computer > 33)) # False
print(not(physics > 33 and computer > 33)) # True

# ========================
#   Assignment Operators
# ========================

a = 10

a += 5
a -= 5
a *= 2
a /= 2
a %= 3
a //= 3
a **= 3

print(a)