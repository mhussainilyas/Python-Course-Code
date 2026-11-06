def calculate_marks(math, english, urdu, physics = 10, history = 0):
    print(f"Math = {math}")
    print(f"English = {english}")
    print(f"Urdu = {urdu}")
    print(f"Physics = {physics}")
    print(f"History = {history}")
    total_marks = math + english + urdu + physics + history
    print(f"Total Marks = {total_marks}")

calculate_marks(90, 80, 65, 71, 89)
calculate_marks(90, 80, 65, 71)
calculate_marks(90, 80, 65)