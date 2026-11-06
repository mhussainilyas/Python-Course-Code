total_marks = int(input("Enter your marks: "))

if total_marks >= 90 and total_marks <= 100:
    print("Grade: A+")
elif total_marks >= 80 and total_marks < 90:
    print("Grade: A")
elif total_marks >= 70 and total_marks < 80:
    print("Grade: B")
elif total_marks >= 60 and total_marks < 70:
    print("Grade: C")
elif total_marks >= 50 and total_marks < 60:
    print("Grade: D")
elif total_marks >= 40 and total_marks < 50:
    print("Grade: E")
elif total_marks >= 0 and total_marks < 40:
    print("Grade: F")
else:
    print("Invalid marks!")

print("Done")