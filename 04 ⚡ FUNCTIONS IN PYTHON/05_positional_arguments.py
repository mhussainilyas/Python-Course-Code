def calculate_marks(math, english, urdu, physics, history):
    print(f"Math = {math}")
    print(f"English = {english}")
    print(f"Urdu = {urdu}")
    print(f"Physics = {physics}")
    print(f"History = {history}")
    total_marks = math + english + urdu + physics + history
    print(f"Total Marks = {total_marks}")

calculate_marks(english = 90, math = 80, urdu = 65, history = 71, physics = 89)
calculate_marks(90, 80, urdu = 65, history = 71, physics = 89)