"""

Task 1

"""


def odd_nums(max_value):
    n = 1
    while n <= max_value:
        yield n
        n += 2

odd_to_17 = odd_nums(17)
print(odd_to_17)