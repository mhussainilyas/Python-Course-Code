# ==============
#   Example 01
# ==============

def sum_of_numbers(n1, n2, n3):
    total = n1 + n2 + n3
    print(f"Total is = {total}")

sum_of_numbers(10, 20, 30)
# print(total) # NameError: name 'total' is not defined

# ==============
#   Example 02
# ==============

def alpha(n1, n2):
    n1 = 100
    n2 = 200
    print(f"n1 = {n1}, n2 = {n2}")

n1 = 10
n2 = 20
alpha(n1, n2)
print(f"n1 = {n1}, n2 = {n2}")
