# ===================
#   Adding Elements
# ===================

fruits = {"apple", "mango"}

# *** add() — adds a single element ***

fruits.add("banana")

# *** update() — adds multiple elements (from any iterable) ***

fruits.update(["grapes", "kiwi"])

# *** Adding a duplicate is silently ignored ***

fruits.add("apple")
print(fruits)

# =====================
#   Removing Elements
# =====================

fruits = {"apple", "mango", "banana", "kiwi"}

# *** remove() — removes the value, raises KeyError if not found ***

fruits.remove("mango")
fruits.remove("grapes")  # KeyError: 'grapes'

# *** discard() — removes if present, no error if not found (safer) ***

fruits.discard("banana")
fruits.discard("grapes")  #  silently does nothing

# *** pop() — removes and returns a random element ***

removed_elem = fruits.pop()
print(f"Element Removed = {removed_elem}")

# *** clear() — removes everything ***

fruits.clear()
print(fruits)
