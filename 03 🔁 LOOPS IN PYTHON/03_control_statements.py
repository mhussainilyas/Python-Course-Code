# ===================
#   BREAK Statement
# ===================

# *** With WHILE Loop ***

i = 1
while i <= 10:
    if i == 5:
        break
    print(i, end=" ")
    i += 1

# *** With FOR Loop ***

for i in range(1, 11, 1):
    if i == 5:
        break
    print(i, end=" ")

# ======================
#   CONTINUE Statement
# ======================

# *** With WHILE Loop ***

i = 0
while i <= 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i, end=" ")

# *** With FOR Loop ***

for i in range(1, 11, 1):
    if i % 2 == 0:
        continue
    print(i, end=" ")