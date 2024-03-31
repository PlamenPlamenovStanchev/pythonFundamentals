# my_dict = {'a': 1, 'b': 2, 'c': 3}
# my_dict['d'] = my_dict.pop('b')
# print(my_dict)



# my_dict = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
# new_dict = {}
# for key, value in my_dict.items():
#     new_dict[key] = sum(value)
#     print(new_dict)


my_dict = {'a': 1, 'b': 2, 'c': 3}
new_dict = {}
for key, value in my_dict.items():
    if value % 2 == 0:
        new_dict.setdefault('even', []).append(key)
    else:
        new_dict.setdefault('odd', []).append(key)

print(new_dict)