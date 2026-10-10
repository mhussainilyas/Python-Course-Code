numbers = range(1, 20)

# =================
#   Basic Example
# =================

print(numbers[2:6])
print(list(numbers[2:6]))

# =======================
#   Slicing with a Step
# =======================

print(list(numbers[2:10:2]))

# ==========================
#   Using Negative Indexes
# ==========================

print(list(numbers[-4: -1]))

# ===================================
#   Reversing a Range Using Slicing
# ===================================

print(list(numbers[::-1]))