nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ====================
#   Using while loop
# ====================

# *** Forward Loop ***

i = 0
n = len(nums)
print("Forward Loop = ", end="")
while i < n:
    print(nums[i], end=" ")
    i += 1

# *** Backward Loop ***

n = len(nums)
i = n - 1
print("Backward Loop = ", end="")
while i >= 0:
    print(nums[i], end=" ")
    i -= 1

# ==================
#   Using for loop
# ==================

# *** Forward Loop ***

n = len(nums)
print("Forward Loop = ", end="")
for i in range(0, n):
    print(nums[i], end=" ")

# *** Backward Loop ***

n = len(nums)
print("Backward Loop = ", end="")
for i in range(n - 1, 0 - 1, -1):
    print(nums[i], end=" ")

# *** Using for-each loop ***

print("Using for-each loop = ", end="")
for num in nums:
    print(num, end=" ")

# *** Using list slicing ***

print("Using list slicing = ", end="")
for num in nums[::-1]:
    print(num, end=" ")

# ==============
#   Example 01
# ==============

marks = [54, 76, 46, 98, 26]

# *** 1st Method ***

# total_marks = 0
# n = len(marks)
# for i in range(0, n):
#     total_marks += marks[i]

# *** 2nd Method ***

total_marks = 0
for mark in marks:
    total_marks += mark

print(f"Total marks = {total_marks}")
