"""
Q53. Given a list of numbers, write Python code using a loop to find and print
the largest element. Do not use the built-in max() function.
"""

# numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# largest_element = numbers[0]
# for num in numbers:
#     if num > largest_element:
#         largest_element = num

# print(f"Largest element = {largest_element}")

"""
Q54. Write a program that takes a list and a target number. 
Use a loop to determine if the target number exists in the list. 
Do not use the in operator.
"""

# def check_target_exists(lt, target_num):
#     for value in lt:
#         if value == target_num:
#             return True
#     return False


# target = 30
# data_list = [10, 20, 30, 40, 50]

# result = check_target_exists(data_list, target)

# if result:
#     print(f"{target} exists in the list.")
# else:
#     print(f"{target} does not exists in the list")

"""
Q55. Given a list of numbers, use a loop to calculate and print their average. 
You can use len() to get the count of elements, but avoid using sum() for the total.
Format the average to two decimal places.
"""

# def calculate_average(nums):
#     n = len(nums)
#     total_score = 0
#     for num in nums:
#         total_score += num
#     return total_score / n

# scores = [85, 90, 78, 92, 98]
# average_score = calculate_average(scores)
# print(f"Score average is = {average_score:.2f}")

"""
Q56. Given two lists of the same length, write Python code using a loop 
to create a new list where each element is the sum of the corresponding elements 
from both original lists.
"""

# def sum_of_two_list(l1, l2):
#     if len(l1) != len(l2):
#         print("Both lists must have same length!")
#         return False
#     resultant_list = []
#     for i in range(0, len(l1), 1):
#         elem_sum = l1[i] + l2[i]
#         resultant_list.append(elem_sum)
#     return resultant_list

# list1 = [1, -2, 3, -4]
# list2 = [10, 20, 30, 40]
# new_list = sum_of_two_list(list1, list2)
# print(f"Element-wise sum list = {new_list}")

"""
Q57. Write a program that takes a list of numbers and, using a loop, determines 
whether it is sorted in ascending order. Print True if it is sorted, and False otherwise.
Do not use built-in sort or sorted() functions for checking.
"""

# def is_sorted(lst):
#     n = len(lst)
#     for i in range(0, n - 1, 1):
#         if lst[i] > lst[i + 1]:
#             return False
#     return True

# numbers = [1, 10, 5, 15, 20]
# result = is_sorted(numbers)
# print(f"Sorted = {result}")
