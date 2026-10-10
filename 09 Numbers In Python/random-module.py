import random

# ===========
#   Methods
# ===========

# print(random.random())
# print(random.uniform(1, 10))
# print(random.randint(1, 10))
# print(random.randrange(1, 10))
# print(random.choice(["HSN", "SLM", "ZRB"]))

# print(random.sample([1, 2, 3, 4, 5], 1))
# print(random.sample([1, 2, 3, 4, 5], 2))
# print(random.sample([1, 2, 3, 4, 5], 3))

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)