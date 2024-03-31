# from functools import reduce
#
# numbers = [1, 2, 3, 4, 5]
# squared = map(lambda x: x**2, numbers)
# result = reduce(lambda x, y: x * y, squared)
# print(result)

# from functools import reduce
# nums = [1, 2, 3, 4, 5]
# result = reduce(lambda x, y: x + y, map(lambda x: x**3, filter(lambda x: x % 2 == 0, nums)))
# print(result)

# data = [1, 2, 3, 4, 5]
# result = [x**2 if x % 2 == 0 else x**3 for x in data if x > 2]
# print(result)

# def custom_func(x):
#     return x if x % 2 == 0 else x**2
#
# data = [1, 2, 3, 4, 5]
# result = reduce(lambda x, y: x + y, map(custom_func, filter(lambda x: x < 5, data)))
# print(result)

from functools import reduce


def custom_func(x):
    return x + 1 if x < 5 else x - 1

data = [1, 2, 3, 4, 5, 6, 7, 8]
result = reduce(lambda x, y: x * y, map(custom_func, filter(lambda x: x % 2 == 0, data)))

print(result)
