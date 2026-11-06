name = "Hussain" # Global variable

def greet(n):
    name = n
    print(f"Hye! {name}")

greet("Ali")
print(name) # Hussain

# ==================
#   Global Keyword
# ==================

count = 0

def increment_count():
    global count
    count += 1
    print(f"Inside function count = {count}")

increment_count()
increment_count()
increment_count()
print(f"Outside function count = {count}")