students = {
    "Hussain": {"math": 87, "science": 92, "english": 74},
    "Suleman": {"math": 65, "science": 78, "english": 90},
    "Zaryab": {"math": 55, "science": 60, "english": 48},
    "Shaoib": {"math": 95, "science": 88, "english": 82},
    "Hamid": {"math": 70, "science": 45, "english": 63},
}

sort_by_math_marks = sorted(students.items(), key=lambda x: x[1]["math"])
sorted_dict = dict(sort_by_math_marks)

sort_by_total_marks = sorted(students.items(), key=lambda x: sum(x[1].values()))
sorted_dict = dict(sort_by_total_marks)

for name, scores in sorted_dict.items():
    print(f"{name} - {scores}")
