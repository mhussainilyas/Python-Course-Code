# ====================
#   Forward For Loop
# ====================

# range(start, end, steps)

for i in range(1, 11):
    print(i, end=" ")

for i in range(1, 11, 3):
    print(i, end=" ")

# =====================
#   Backward For Loop
# =====================

for i in range(10, 0, -1):
    print(i, end=" ")

for i in range(10, 0, -3):
    print(i, end=" ")

# ==============
#   Example 01
# ==============

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for i in range(start, end + 1, 1):
    if i % 2 == 0:
        print(i, end=" ")

    