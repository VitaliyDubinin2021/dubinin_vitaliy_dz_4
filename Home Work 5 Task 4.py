"""
Task 4

"""

src = [500, 5, 17, 49, 2, 3, 76, 551, 25, 3, 99, 15, 178]
new_list = [num for i, num in enumerate(src) if num > src[i - 1] and i != 0]
print(new_list)