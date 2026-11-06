# ===================
#   Example Code 01
# ===================

marks = {
    "math": 85,
    "science": 92,
    "english": 60,
    "urdu": 78,
}

result = sorted(marks.items(), key=lambda x: x[1])

sorted_dict = dict(result)

# ===================
#   Example Code 02
# ===================

marks = {
    "Hussain": [43, 12, 98, 10, 22],
    "Suleman": [76, 55, 34, 89, 61],
    "Zaryab": [20, 45, 67, 30],
    "Shoaib": [91, 73],
    "Hamid": [38, 82, 47, 95, 29],
}

sort_by_last_mark = sorted(marks.items(), key=lambda x: x[1][-1])
sorted_dict = dict(sort_by_last_mark)

sort_by_sum_of_marks = sorted(marks.items(), key=lambda x: sum(x[1]), reverse=True)
sorted_dict = dict(sort_by_sum_of_marks)

for name, scores in sorted_dict.items():
    print(f"{name} - {scores}")

print(f"sorted dict = {sorted_dict}")
