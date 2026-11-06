def find_square(num):
    return num ** 2

def find_sum_of_squares(n1, n2):
    return find_square(n1) + find_square(n2)

result = find_sum_of_squares(3, 4)
print(f"The sum of squares of 3 and 4 is: {result}")