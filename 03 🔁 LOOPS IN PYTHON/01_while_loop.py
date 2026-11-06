# ======================
#   Forward While Loop
# ======================

i = 1

while i <= 10:
    print(f"Iteration number {i}")
    i += 1

print("Done")

# =======================
#   Backward While Loop
# =======================

i = 10

while i >= 1:
    print(i, end=" ")
    i -= 1

print("Done")

# ==============
#   Example 02
# ==============

count = 1

while count <= 10:
    print(count)
    count += 1
    print("Hussain")

print("Done")

# ==============
#   Example 03
# ==============

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

i = start
while i <= end:
    print(i, end=" ")
    i += 1

print(f"After while loop, start value is = {start}")
print(f"After while loop, end value is = {end}")
print(f"After while loop, i value is = {i}")

# ==============
#   Example 04
# ==============

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

i = start
while i <= end:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1

print("Done")