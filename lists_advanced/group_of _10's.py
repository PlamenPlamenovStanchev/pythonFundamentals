# list_of_numbers = input().split(", ")
# numbers = sorted(map(int, list_of_numbers))
# result = []
# current_group = None
# current_group_numbers = []
# for num in numbers:
#     group = (num // 10) * 10
#     if  current_group is None or group == current_group:
#         current_group_numbers.append(num)
#     else:
#         result.append((current_group, current_group_numbers))
#         current_group_numbers = [num]
#     current_group = group
# for group, group_numbers in result:
#     print(f"Group of {group}'s:{group_numbers}")



numbers = [int(number) for number in input().split(", ")]
current_group = 10
while numbers:
    filtered_numbers_of_current_group = [number for number in numbers if number <= current_group]
    print(f"Group of {current_group}'s: {filtered_numbers_of_current_group}")
    current_group += 10
    numbers = [number for number in numbers if number not in filtered_numbers_of_current_group]