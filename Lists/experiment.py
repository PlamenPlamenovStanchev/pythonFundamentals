# my_list = [1, 2, 3, 4, 5]
# print(sum(my_list))
# print(len(my_list))
# if 0 in my_list:
#     print("the number 0 is in your list")
# else:
#     print("the number 0 is not on your list")

# words = ['apple', 'banana', 'cherry', 'date']
# result = []
# for word in words:
#     if len(word) > 5:
#         result.append(word[::-1])
#
# print(result)

# original_list = [1, 2, 3, 4, 5]
# doubled = map(lambda x: x * 2, original_list)
# result = list(doubled)
# print(result)

numbers = [2, 4, 6, 8, 10]
result = [i for i in numbers if all(i % j != 0 for j in range(2, i))]
print(result)