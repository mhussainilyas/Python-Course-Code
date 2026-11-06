data_list = ["Hussain", "Zaryab", 56, 91.8120, 100, "Suleman"]
print(f"Data List = {data_list}")

# =====================
#   Positive Indexing
# =====================

print(f"Element at index 0 = {data_list[0]}")
print(f"Element at index 5 = {data_list[5]}")

# =====================
#   Negative Indexing
# =====================

print(f"Element at index -1 = {data_list[-1]}")
print(f"Element at index -5 = {data_list[-5]}")

# ==================================
#   Accessing Last Element of List
# ==================================

# *** 1st Method ***

n = len(data_list)
print(f"Accessing last element = {data_list[n - 1]}")

# *** 2nd Method ***
print(f"Accessing last element = {data_list[-1]}")

# =================================
#   Updating Elements Using Index
# =================================

data_list[1] = True
data_list[-2] = "ABCD"
print(f"Updated Data List = {data_list}")