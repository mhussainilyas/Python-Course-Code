# ===================
#   Creating Tuples
# ===================

data_set = (1, 2, 3, "HSN")

print(data_set)
print(type(data_set))

# ============
#   Indexing
# ============

data_set = (1, 2, 3, "HSN")

print(data_set[0])
print(data_set[3])
print(data_set[-1])
print(data_set[-3])

# =============
#   Immutable
# =============

my_data = (1, 2, 3, 4)

my_data[0] = 100  # TypeError

# ===========
#   Slicing
# ===========

sample_data = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

sub_sample_data_1 = sample_data[0:4]
sub_sample_data_2 = sample_data[0:6:2]
sub_sample_data_3 = sample_data[::2]
sub_sample_data_4 = sample_data[9:6:-1]
sub_sample_data_5 = sample_data[9::-1]
sub_sample_data_6 = sample_data[::-1]

print(sub_sample_data_3)

# ===========
#   Methods
# ===========

my_data = (1, 2, 3, 4, 1, "HSN", 5, 6, 9, 2, 1)

print(my_data.count(1))
print(my_data.index("HSN"))
