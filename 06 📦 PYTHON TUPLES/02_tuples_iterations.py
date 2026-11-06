sample_data = (100, 200, 300, "HSN", True, 3.47, "JVR")

# ==============
#   While loop
# ==============

i = 0
n = len(sample_data)
while i < n:
    print(sample_data[i], end=" ")
    i += 1

# ============
#   For loop
# ============

# *** 1st Method ***

n = len(sample_data)
for i in range(0, n):
    print(sample_data[i], end=" ")

# # *** 2nd Method ***

for elem in sample_data:
    print(elem, end=" ")

# ===============
#   enumerate()
# ===============

print()
for index, elem in enumerate(sample_data):
    print(f"index is = {index} and value is = {elem}")
