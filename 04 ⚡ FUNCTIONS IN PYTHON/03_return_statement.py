def sum_of_numbers(n1, n2, n3):
    ans = n1 + n2 + n3
    return ans

def count_factors(n):
    count = 0
    for i in range(1, n + 1, 1):
        if n % i == 0:
            count += 1
    return count

result = sum_of_numbers(4, 10, 6)
total_factors = count_factors(result)
print(f"total factors of {result} are = {total_factors}")