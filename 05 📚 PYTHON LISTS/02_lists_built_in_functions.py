marks = [45, 34, 54, 65, 23, 65, 76, 91]

# ===== len() - Get Length =====
list_length = len(marks)
print(f"Length = {list_length}")

# ===== max() - Get Maximum Value =====
max_value = max(marks)
print(f"Maximum Value = {max_value}")

# ===== min() - Get Minimum Value =====
min_value = min(marks)
print(f"Minimum Value = {min_value}")

# ===== sum() - Get Sum of All Elements =====
total = sum(marks)
print(f"Sum = {total}")

# ===== sorted() - Create Sorted List =====
sorted_marks = sorted(marks)
print(f"Sorted List = {sorted_marks}")
reverse_sorted_marks = sorted(marks, reverse=True)
print(f"Reverse Sorted List = {reverse_sorted_marks}")
