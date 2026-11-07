fruits = {"apple", "mango", "banana"}

# ===================
#   Simple for loop
# ===================

for fruit in fruits:
    print(fruit)

# ==============================================================
#   Looping with enumerate (rarely needed for sets, but works)
# ==============================================================

for index, fruit in enumerate(fruits, start=1):
    print(f"index is = {index} and fruit is = {fruit}")

# =======================================
#   Practical Application: Unique Words
# =======================================

sentence = "python is fun and python is powerful"
words = set(sentence.split())

for word in words:
    print(word)
