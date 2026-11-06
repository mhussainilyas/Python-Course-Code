"""
Q74: Create a tuple of 5 of your favourite songs. Print the first, last,
and middle one using indexing
"""

# fav_songs = ("Dilawara", "Parano", "Ride-It", "Heeriye", "No-Love")

# n = len(fav_songs)
# print(f"first song = {fav_songs[0]}")
# print(f"first song = {fav_songs[-1]}")
# print(f"first song = {fav_songs[n // 2]}")

"""
Q75: Create a tuple of 8 numbers. Using slicing, print the first 3, last 3, 
and every alternate element.
"""

# numbers = (100, 200, 300, 400, 500, 600, 700, 800)

# first_3_nums = numbers[0:3]
# last_3_nums = numbers[:-4:-1]
# alternative_nums = numbers[::2]

# print(f"first 3 numbers = {first_3_nums}")
# print(f"last 3 numbers = {last_3_nums}")
# print(f"alternative elements = {alternative_nums}")

"""
Q76: Create a tuple of marks of 6 students. Print the highest, lowest, total, 
and average.
"""

# marks = (76, 65, 48, 32, 91, 50)

# n = len(marks)
# highest = max(marks)
# lowest = min(marks)
# total = sum(marks)
# average = total / n

# print(f"Highest marks = {highest}")
# print(f"Lowest marks = {lowest}")
# print(f"Total marks = {total}")
# print(f"Average marks = {average:.2f}")

"""
Q77: Take 5 numbers as input from the user, store them in a tuple, 
and print the tuple along with its minimum and maximum.
"""

# num_1 = int(input("Enter 1st number: "))
# num_2 = int(input("Enter 2nd number: "))
# num_3 = int(input("Enter 3rd number: "))
# num_4 = int(input("Enter 4th number: "))
# num_5 = int(input("Enter 5th number: "))

# nums_tuple = num_1, num_2, num_3, num_4, num_5

# print(f"Tuple = {nums_tuple}")
# print(f"Maximum = {max(nums_tuple)}")
# print(f"Minimum = {min(nums_tuple)}")

"""
Q78: Write a function get_stats(nums) that takes a tuple of numbers and returns 
a tuple containing the sum, average, minimum, and maximum. Unpack
the returned tuple and print each value.
"""


# def get_stats(nums):
#     n = len(nums)
#     maximum = max(nums)
#     minimum = min(nums)
#     total = sum(nums)
#     average = total / n
#     return maximum, minimum, total, average


# marks = (76, 65, 48, 32, 91, 50)

# maxi, mini, total, avg = get_stats(marks)

# print(f"Maximum = {maxi}")
# print(f"Minimum = {mini}")
# print(f"Total = {total}")
# print(f"Average = {avg:.2f}")
