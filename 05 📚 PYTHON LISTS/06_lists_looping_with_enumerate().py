marks = [56, 78, 92, 51, 46, 26]

# ==============================
#   Basic Usage of enumerate()
# ==============================

for index, mark in enumerate(marks):
    print(f"Index = {index} and Value = {mark}")

# =======================================
#   enumerate() with Custom Start Index
# =======================================

for index, mark in enumerate(marks, start=2):
    print(f"Index = {index} and Value = {mark}")
