"""
Q58. Find the largest and smallest number
in a list without using built-in functions like
max() or min().
"""

# def find_max_min(lst):
#     largest_element = lst[0]
#     smallest_element = lst[0]
#     for value in lst:
#         if value > largest_element:
#             largest_element = value
#         if value < smallest_element:
#             smallest_element = value
#     return [smallest_element, largest_element]

# numbers = [3, 1, 4, 1, -5]
# result = find_max_min(numbers)
# print(f"Smallest is = {result[0]}")
# print(f"Largest is = {result[1]}")

"""
Q59. Reverse a list without using the
.reverse() method or list slicing ([::-1]).
"""

# def reverse_list(lst):
#     n = len(lst)
#     new_list = []
#     for i in range(n - 1, 0 - 1, -1):
#         new_list.append(lst[i])
#     return new_list

# data_list = [40, 10, 30, 20, 50]
# new_data_list = reverse_list(data_list)
# print(f"Reverse List = {new_data_list}")

"""
Q60. Given two lists, merge them into a
single new list without modifying the originals.
"""

# =============
#  1st Method
# =============

# def merge_two_list(l1, l2):
#     return l1 + l2

# =============
#  2nd Method
# =============

# def merge_two_list(l1, l2):
#     new_list = []
#     for value in l1:
#         new_list.append(value)
#     for value in l2:
#         new_list.append(value)
#     return new_list

# ===============
#   Driver Code
# ===============

# list1 = [1, 2, 3, "HSN"]
# list2 = [4, 5, "Male", 6]
# new_list = merge_two_list(list1, list2)
# print(f"Merged List = {new_list}")

"""
Q61. Given a list, remove all duplicate elements while
preserving the original order of the unique items
"""


# def remove_duplicate_element(lst):
#     new_list = []
#     for value in lst:
#         if value not in new_list:
#             new_list.append(value)
#     return new_list

# data_list = [1, 2, 3, 1, 4, 2, 3, 1, 3, 2, 5]
# print(f"Original List = {data_list}")

# new_data_list = remove_duplicate_element(data_list)
# print(f"Unique List = {new_data_list}")

"""
Q62. Separate a list of integers into two distinct lists: one
containing all the even numbers and the other
containing all the odd numbers
"""

# def even_odd_list(lst):
#     odd_list = []
#     even_list = []
#     for num in lst:
#         if num % 2 == 0:
#             even_list.append(num)
#         else:
#             odd_list.append(num)
#     return even_list, odd_list

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# res1, res2 = even_odd_list(numbers)
# print(f"Even Numbers = {res1}")
# print(f"Odd Numbers = {res2}")

"""
Q63. Create a list containing the squares of numbers
from 1 to 10 (i.e., [1, 4, 9, ..., 100]).
"""

# def square_list(lst):
#     new_list = []
#     for num in lst:
#         ans = num**2
#         new_list.append(ans)
#     return new_list

# numbers = [1, 2, 3, 4, 5]
# result = square_list(numbers)
# print(f"Square List = {result}")

"""
Q64. Given a list of numbers (which may contain duplicates), write a
Python script that takes an integer as input from the user and
removes all occurrences of that integer from the list.
"""

# ===============
#   Solution 01
# ===============

# def remove_occurence(lst, target):
#     new_list = []
#     for elem in lst:
#         if elem != target:
#             new_list.append(elem)
#     return new_list

# integer = int(input("Enter an integer: "))
# numbers = [1, 2, 3, 4, 5, 1, 2, 6, 7, 3, 8, 2, 9, 3, 5, 10]
# new_numbers = remove_occurence(numbers, integer)
# print(f"List not containing {integer} is = {new_numbers}")

# ===============
#   Solution 02
# ===============

# def remove_occurence(lst, target):
#     while target in lst:
#         lst.remove(target)

# integer = int(input("Enter an integer: "))
# numbers = [1, 2, 3, 4, 5, 1, 2, 6, 7, 3, 8, 2, 9, 3, 5, 10]
# remove_occurence(numbers, integer)
# print(numbers)

"""
Q65. Write a Python script that iterates through a list of integers and
replaces every negative number found in the list with the value 0.
"""

# def replace_negative(lst):
#     for i, num in enumerate(lst):
#         if num < 0:
#             lst[i] = 0
#     return lst

# numbers = [1, 2, 3, 4, -5, -1, -3, 6, 8, -9, 10]
# new_numbers_list = replace_negative(numbers)
# print(f"List without negative numbers = {new_numbers_list}")