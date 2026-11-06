matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(matrix[0])
print(matrix[0][0])
print(matrix[0][1])
print(matrix[0][2])
print(matrix[1][0])
print(matrix[1][1])
print(matrix[1][2])
print(matrix[2][0])
print(matrix[2][1])
print(matrix[2][2])

# =========================
#   Loop with nested list
# =========================

# *** 1st Method ***

for i in range(0, 3):
    for j in range(0, 3):
        print(matrix[i][j], end=" ")
    print()

# *** 2nd Method ***

rows = len(matrix)
for i in range(0, rows):
    cols = len(matrix[i])
    for j in range(0, cols):
        print(matrix[i][j], end=" ")
    print()

# *** 3rd Method ***

for row in matrix:
    for val in row:
        print(val, end=" ")
    print()
