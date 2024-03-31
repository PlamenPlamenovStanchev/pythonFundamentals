# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# result = fibonacci(5)
# print(result)

# def even_or_odd(n):
#     return "Even" if n % 2 == 0 else "Odd"
#
 # print(even_or_odd(2) == even_or_odd(3))

# def func():
#     return [lambda x: x * i for i in range(5)]
#
# results = [m(2) for m in func()]
# print(results)

# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Before calling function")
#         result = func(*args, **kwargs)
#         print("After calling function")
#         return result
#     return wrapper
#
# @my_decorator
# def my_function(x):
#     return x * 2
#
# result = my_function(5)
# print(result)