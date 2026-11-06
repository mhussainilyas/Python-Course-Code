#       +0  +1  +2  +3  +4  +5  +6  +7  +8   +9
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#      -10  -9  -8  -7  -6  -5  -4  -3  -2   -1

# ===================
#   Forward Slicing
# ===================

num_list_1 = nums[0:4]
num_list_2 = nums[5:8]
num_list_3 = nums[1:9]
num_list_4 = nums[1:100]
num_list_5 = nums[5:6]
num_list_6 = nums[5:5]
num_list_7 = nums[4:-1]

num_list_8 = nums[4:]
num_list_9 = nums[:7]

num_list_10 = nums[1:-1:2]
num_list_11 = nums[0::2]
num_list_12 = nums[:7:2]
num_list_13 = nums[::3]

# ====================
#   Backward Slicing
# ====================

num_list_14 = nums[9:2:-1]
num_list_15 = nums[5::-1]
num_list_16 = nums[::-1]
num_list_17 = nums[::-2]

print(f"Output = {num_list_17}")
