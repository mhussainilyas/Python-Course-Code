name = "Hussain"
gender = "male"
age = 21

print("Hye!", name, "your age is", age, "your gender is", gender)

print("Hye! " + name + " your gender is " + gender)

print(name, age, gender, sep=" ")
print(name, age, gender, sep="abc")
print(name, age, gender, sep="-")

print(name, end=" | ")
print(gender, end=" | ")
print(age)

# =============
#   F-Strings
# =============

print(f"Hye! {name} your age is {age} your gender is {gender}")
print(f"Hye! {name} your age is {age - 10} your gender is {gender}")