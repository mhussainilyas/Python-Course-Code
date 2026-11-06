age = 21
has_degree = True

if age >= 18:
    print("Age requirement met.")
    if has_degree == True:
        print("You are eligible for this job.")
    else:
        print("You need a degree for this job!")
else:
    print("You are too young to apply!")

print("Done")

# ===================
#   Another Example
# ===================

cgpa = 3.47
has_domicile = True

if cgpa < 2.0:
    pass
else:
    if cgpa > 3:
        print("cgpa requirement met.")
        if has_degree == True:
            print("You can enroll for scholorship.")
        else:
            print("Domicile is required!")
    else:
        print("cgpa is too low, not eligible!")