# ==============
#   Example 01
# ==============

# *** NORMAL FUNCTION ***

def find_square(num):
    return num ** 2

print(f"square of 5 is = {find_square(5)}")

# *** LAMBDA FUNCTION ***

get_square = lambda num: num ** 2
print(f"square of 6 is = {get_square(6)}")

# ==============
#   Example 02
# ==============

# *** NORMAL FUNCTION ***

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else: 
        return "Odd"

print(f"check_even_odd(5) = {check_even_odd(5)}")
print(f"check_even_odd(6) = {check_even_odd(6)}")

# *** LAMBDA FUNCTION ***

is_even_odd = lambda num: "Even" if num % 2 == 0 else "Odd"
print(f"is_even_odd(10) = {is_even_odd(10)}")
print(f"is_even_odd(11) = {is_even_odd(11)}")