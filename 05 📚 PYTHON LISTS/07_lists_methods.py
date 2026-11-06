data_list = ["Hussain", 595, 3.47, "HSN", True, "Male", "HSN"]
print(f"Original List = {data_list} with id ={id(data_list)}")

# ==========================
#   .append() - Add to End
# ==========================

# data_list.append(100)

# ============================
#   .insert() - Add at Index
# ============================

# data_list.insert(2, "Lahore")

# ===============================
#   .remove() - Remove by Value
# ===============================

# data_list.remove("Male")

# ======================================
#   .pop() - Remove by Index (or Last)
# ======================================

# popped_element = data_list.pop()
# popped_element = data_list.pop(0)
# popped_element = data_list.pop(3)
# print(f"Popped Element = {popped_element}")

# ===========================
#   .sort() - Sort In-Place
# ===========================

# num_list = [10, 265, 18, 6, 7253]
# str_list = ["Hussain", "Ali", "Ahmad"]

# print(f"Original List = {num_list} with id ={id(num_list)}")
# print(f"Original List = {str_list} with id ={id(str_list)}")

# str_list.sort()
# num_list.sort(reverse=True)

# print(f"Updated List = {num_list} with id ={id(num_list)}")
# print(f"Updated List = {str_list} with id ={id(str_list)}")

# =================================
#   .reverse() - Reverse In-Place
# =================================

# data_list.reverse()

# =================================
#   .index() - Find Element Index
# =================================

# element_index = data_list.index("Male")
# print(f"Index value of 'Hussain' is = {element_index}")

# ========================================
#   .count() - Count Element Occurrences
# ========================================

# total_occurrence = data_list.count("HSN")
# print(f"'HSN' occurs {total_occurrence} times")

# ==================================
#   .clear() - Remove All Elements
# ==================================

data_list.clear()

# ===================================
#   .copy() - Create a Shallow Copy
# ===================================

# new_data_list = data_list.copy()
# print(f"Copied List = {new_data_list} with id ={id(new_data_list)}")


print(f"Updated List = {data_list} with id ={id(data_list)}")
