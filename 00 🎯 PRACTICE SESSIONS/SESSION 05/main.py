"""
Q21. Print the pattern
*
* *
* * *
* * * *
* * * * *
"""

# for i in range(1, 6, 1):
#     for j in range(1, i + 1, 1):
#         print("*", end=" ")
#     print()

"""
Q22. Print the pattern
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

# for i in range(1, 6, 1):
#     for j in range(1, i + 1, 1):
#         print(j, end=" ")
#     print()

"""
Q23. Print the pattern
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
"""

# for i in range(1, 6, 1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()

"""
Q24. Print the pattern
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

# for i in range(5, 0, -1):
#     for j in range(1, i + 1, 1):
#         print(j, end=" ")
#     print()

"""
Q25. Print the pattern
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""

# n = int(input("Enter number: "))

# for i in range(1, n + 1, 1):
#     for j in range(n, i - 1, -1):
#         print(j, end=" ")
#     print()

"""
Q26. Print the pattern
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""

# for i in range(5, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()

"""
Q27. Print the pattern
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

# for i in range(1, 6, 1):
#     for j in range(1, i + 1, 1):
#         print(j, end=" ")
#     print()

# for i in range(4, 0, -1):
#     for j in range(1, i + 1, 1):
#         print(j, end=" ")
#     print()

"""
Q28. Print the pattern
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""

# for i in range(5, 0, -1):
#     for j in range(5, i - 1, -1):
#         print(j, end=" ")
#     print()

# for i in range(2, 6, 1):
#     for j in range(5, i - 1, -1):
#         print(j, end=" ")
#     print()

"""
Q29. Print the pattern
        1
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9
  1 2 3 4 5 6 7
    1 2 3 4 5
      1 2 3
        1
"""

# for i in range(1, 6, 1):
#     for k in range(1, 5 - i + 1, 1):
#         print(" ", end=" ")
#     for j in range(1, (i * 2 - 1) + 1, 1):
#         print(j, end=" ")
#     print()

# for i in range(4, 0, -1):
#     for k in range(1, 5 - i + 1, 1):
#         print(" ", end=" ")
#     for j in range(1, (i * 2 - 1) + 1, 1):
#         print(j, end=" ")
#     print()

"""
Q30. Print the pattern
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
"""

# for i in range(1, 6, 1):
#     for k in range(1, 5 - i + 1, 1):
#         print(" ", end=" ")
#     for j in range(1, (i * 2 - 1) + 1, 1):
#         print("*", end=" ")
#     print()

# for i in range(4, 0, -1):
#     for k in range(1, 5 - i + 1, 1):
#         print(" ", end=" ")
#     for j in range(1, (i * 2 - 1) + 1, 1):
#         print("*", end=" ")
#     print()

"""
Q31. Print the pattern
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""

# num = 1
# for i in range(1, 6, 1):
#     for j in range(1, i + 1, 1):
#         print(num, end=" ")
#         num += 1
#     print()

"""
Q32. Print the pattern
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""

# for i in range(1, 6, 1):
#     for j in range(1, 6, 1):
#         print(j, end=" ")
#     print()

"""
Q33. Print the pattern
* * * * *
*       *
*       *
*       *
* * * * *
"""

# for i in range(1, 6, 1):
#     for j in range(1, 6, 1):
#         if i == 1 or i == 5 or j == 1 or j == 5:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

"""
Q34. Print the pattern
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
"""

# for i in range(1, 6, 1):
#     for j in range(1, 6, 1):
#         if (i + j) % 2 == 0:
#             print("1", end=" ")
#         else: 
#             print("0", end=" ")
#     print()