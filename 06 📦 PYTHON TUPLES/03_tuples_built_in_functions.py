# =============================
#   Basic Aggregate Functions
# =============================

python_marks = (85, 92, 78, 95, 60, 88)

print(len(python_marks))  # 6 — number of elements
print(min(python_marks))  # 60 — smallest value
print(max(python_marks))  # 95 — largest value
print(sum(python_marks))  # 498 — sum of all elements

# ==================
#   Sorting Tuples
# ==================

nums = (40, 10, 30, 20, 50)

result = sorted(nums)

print(result)
print(type(result))  # <class 'list'>

# *** sorted result as a tuple ***

sorted_tuple = tuple(sorted(nums))
print(sorted_tuple)
print(type(sorted_tuple))

# *** Reverse Sorting ***

reverse_sort = sorted(nums, reverse=True)
print(reverse_sort)

