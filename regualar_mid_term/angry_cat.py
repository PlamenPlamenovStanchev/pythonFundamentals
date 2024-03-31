# def calculate_damage(items, entry_point, item_type):
#     left_damage = 0
#     right_damage = 0
#
#     for i in range(len(items)):
#         if i < entry_point:
#             if item_type == "cheap" and items[i] < items[entry_point]:
#                 left_damage += items[i]
#         elif i > entry_point:
#             if item_type == "cheap" and items[i] < items[entry_point]:
#                 right_damage += items[i]
#             elif item_type == "expensive" and items[i] >= items[entry_point]:
#                 right_damage += items[i]
#
#     if left_damage >= right_damage:
#         return f"Left - {left_damage}"
#     else:
#         return f"Right - {right_damage}"
#
# items = list(map(int, input().split(", ")))
# entry_point = int(input())
# item_type = input()
#
# result = calculate_damage(items, entry_point, item_type)
# print(result)


# items = list(map(int, input().split(", ")))
# entry_point = int(input())
# item_type = input()
#
#
# left_damage = sum(items[i] for i in range(entry_point) if item_type == "cheap" and items[i] < items[entry_point])
# right_damage = sum(items[i] for i in range(entry_point + 1, len(items))
#                    if (item_type == "cheap" and items[i] < items[entry_point]) or
#                       (item_type == "expensive" and items[i] >= items[entry_point]))
#
#
# if left_damage >= right_damage:
#     print(f"Left - {left_damage}")
# else:
#     print(f"Right - {right_damage}")


# items = list(map(int, input().split(", ")))
# entry_point = int(input())
# item_type = input()
#
# left_damage = 0
# right_damage = 0
#
# for i in range(entry_point):
#     if item_type == "cheap" and items[i] < items[entry_point]:
#         left_damage += items[i]
#
# for i in range(entry_point + 1, len(items)):
#     if (item_type == "cheap" and items[i] < items[entry_point]) or \
#        (item_type == "expensive" and items[i] >= items[entry_point]):
#         right_damage += items[i]
#
#
# if left_damage >= right_damage:
#     print(f"Left - {abs(left_damage)}")
# else:
#     print(f"Right - {abs(right_damage)}")



price_ratings = list(map(int, input().split(", ")))
entry_point = int(input())
item_type = input()


left_damage = 0
right_damage = 0


for i in range(entry_point - 1, -1, -1):
    if item_type == "cheap" and price_ratings[i] < price_ratings[entry_point]:
        left_damage += price_ratings[i]
    elif item_type == "expensive" and price_ratings[i] >= price_ratings[entry_point]:
        left_damage += price_ratings[i]
    else:
        break

for i in range(entry_point + 1, len(price_ratings)):
    if item_type == "cheap" and price_ratings[i] < price_ratings[entry_point]:
        right_damage += price_ratings[i]
    elif item_type == "expensive" and price_ratings[i] >= price_ratings[entry_point]:
        right_damage += price_ratings[i]
    else:
        break


if left_damage >= right_damage:
    print(f"Left - {left_damage}")
else:
    print(f"Right - {right_damage}")