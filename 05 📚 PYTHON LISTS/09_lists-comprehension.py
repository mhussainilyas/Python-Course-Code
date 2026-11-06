# ==============================
#   Without List Comprehension
# ==============================

new_list = []
for i in range(1, 11):
    new_list.append(i)

# ===========================
#   With List Comprehension
# ===========================

new_list = [i for i in range(1, 11)]

# ================
#   Example Code
# ================

new_list_1 = [i for i in range(10, 0, -1)]

new_list_2 = [i + 7 for i in range(1, 11)]
new_list_3 = [i**2 for i in range(1, 11)]

new_list_4 = [i for i in range(1, 11) if i % 2 == 0]
new_list_5 = [i for i in range(1, 51) if i % 3 == 0 and i % 7 == 0]

# =================================================
#   From 1 to 100, make list of all prime numbers
# =================================================


def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        return True
    return False


prime_list = [i for i in range(2, 101) if is_prime(i)]

print(f"prime numbers from 1 to 100 are = {prime_list}")
