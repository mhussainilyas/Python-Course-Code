# ===============
#   1) Integers
# ===============
# whole numbers
# non-decimal values
# negative or positive

age = 21
amount = 999
total_students = 76
temperature = -28

print(type(temperature))

# ============
#   2) Float
# ============
# decimal numbers
# positive or negative
# can contain fractions

price = 19.999
lose = -10.5
weight = 54.81
height = 5.8

print(type(height))

# ======================
#   3) Complex Numbers
# ======================
# real and imaginary values
# written with "j"
# example: 3 + 2j

number = 4 + 7j

print(type(number))

# =====================
#   4) Boolean (bool)
# =====================
# represents True or False
# used for conditions
# only two values: True (1), False (0)

is_loggedIn = True
is_admin = False
has_Identity = False

print(type(has_Identity))

# ==============
#   5) Strings
# ==============
# sequence of characters
# written inside quotes
# text or characters

learner = "Hussain"
course = 'Python Language'
full_name = "Muhammad Hussain"

message = '''
This is
multiple
line string
message
'''

description = """
This is
a long
description
text
"""

print(type(message))

# ======================
#   6) NoneType (None)
# ======================
# represents no value
# used when value is unavailable
# only one value: None

teacher = None
selected_products = None

print(type(selected_products))

# ============
#   7) Bytes
# ============
# stores binary data
# immutable sequence of bytes
# used for binary files/data

b = b"Hello"
data_bytes = bytes([65, 66, 67])

print(b)
print(data_bytes)
print(type(data_bytes))