# ==========
#   abs(x)
# ==========

x = -10
result_x = abs(x)
print(result_x)

# ============
#   round(x)
# ============

a = 3.899999
result_a = round(a)
print(result_a)

print(round(3.234234234, 2)) # 3.23
print(round(3.999999999, 2)) # 4.0
print(round(3.888888888, 2)) # 3.89
print(round(3.499999999, 2)) # 3.5

num = 9.2342342
print(f"result = {num:.2f}") # result = 9.23

# =======================
#   pow(base, exponent)
# =======================

power_result = pow(2, 3) # 2^3
print(power_result)

# =======================
#   min(x1, x2, x3,...)
# =======================

min_val = min(10, 20, 5, -1)
print(min_val)

# =======================
#   max(x1, x2, x3,...)
# =======================

max_val = max(10, 20, 5, -1)
print(max_val)

# =============
#   sum(list)
# =============

numbers = [10, 20, 30]
sum_of_numbers = sum(numbers)
print(sum_of_numbers)

# ==================
#   divmod(x1, x2)
# ==================

# div_mod_result = divmod(17, 5)
quotient, remainder = divmod(17, 5)
print(f"quotient = {quotient} and remainder = {remainder}")

