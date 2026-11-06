"""
Q68. Create a 3x3 matrix (a nested list) and then use nested loops to calculate
and print the sum of all its elements
"""

# def sum_of_all_elem(nes_list):
#     total_sum = 0
#     for rows in nes_list:
#         for elem in rows:
#             total_sum += elem
#     return total_sum


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]

# result = sum_of_all_elem(matrix)
# print(f"sum is = {result}")

"""
Q69. Given a 3x3 matrix as input, print its lower triangle. 
Replace all elements in the upper triangle (above the main diagonal) 
with an asterisk (*).
1 * * 
4 5 * 
7 8 9
"""

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]

# rows = len(matrix)
# cols = len(matrix[0])

# for i in range(0, rows):
#     for j in range(0, cols):
#         if i >= j:
#             print(matrix[i][j], end=" ")
#         else:
#             print("*", end=" ")
#     print()

"""
Q70. Given a 3x3 matrix, print its upper triangle. Replace all elements in
the lower triangle (below the main diagonal) with an asterisk (*).
1 2 3
* 5 6
* * 9
"""

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]

# rows = len(matrix)
# cols = len(matrix[0])

# for i in range(0, rows):
#     for j in range(0, cols):
#         if i <= j:
#             print(matrix[i][j], end=" ")
#         else:
#             print("*", end=" ")
#     print()

"""
Q71. Given a 3x3 matrix, print only the main diagonal elements and
replace everything else with an asterisk (*).
1 * *
* 5 *
* * 9
"""

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]

# rows = len(matrix)
# cols = len(matrix[0])

# for i in range(0, rows):
#     for j in range(0, cols):
#         if i == j:
#             print(matrix[i][j], end=" ")
#         else:
#             print("*", end=" ")
#     print()

"""
Q72. Given a 3x3 matrix, print only the anti-diagonal (top-right to bottom-left)
elements and replace everything else with an asterisk (*).
* * 3
* 5 *
7 * *
"""

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]

# rows = len(matrix)
# cols = len(matrix[0])

# for i in range(0, rows):
#     for j in range(0, cols):
#         if i + j == cols - 1:
#             print(matrix[i][j], end=" ")
#         else:
#             print("*", end=" ")
#     print()

"""
Q73. Given a 4x4 matrix, print only the border elements and replace the inner
elements with an asterisk (*).
1 2 3 4
5 * * 8
9 * * 12
13 14 15 16
"""

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16],
# ]

# rows = len(matrix)
# cols = len(matrix[0])

# for i in range(0, rows):
#     for j in range(0, cols):
#         if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
#             print(matrix[i][j], end=" ")
#         else:
#             print("*", end=" ")
#     print()
