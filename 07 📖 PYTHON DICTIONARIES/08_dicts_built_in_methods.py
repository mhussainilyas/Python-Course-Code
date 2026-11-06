marks = {
    "math": 85,
    "science": 92,
    "english": 78,
    "urdu": 60,
}

# ======================================
#    len() — number of key-value pairs
# ======================================

n = len(marks)

# ===================
#   sum() on values
# ===================

total_marks = sum(marks.values())

# =============================
#   min() and max() on values
# =============================

min_mark = min(marks.values())
max_mark = max(marks.values())

# ============================================================================
#   min() and max() on keys (by default it uses keys, sorted alphabetically)
# ============================================================================

min_mark_in_subj = min(marks)  # english
max_mark_in_subj = max(marks)  # urdu

# ====================================================
#   sorted() on keys — returns a sorted list of keys
# ====================================================

sort_keys = sorted(marks)

# ***  Sorted dictionary by keys ***

sorted_by_keys = dict(sorted(marks.items()))


print(sorted_by_keys)
