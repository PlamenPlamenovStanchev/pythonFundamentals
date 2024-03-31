# n = int(input())
# for num in range(1, n+1):
#     sum_of_digits = 0
#     digits = num
#     while digits > 0:
#         sum_of_digits += digits % 10
#         digits = int(digits/10)
#     if (sum_of_digits ==5) or(sum_of_digits == 7) or (sum_of_digits == 11):
#         print(f"{num} -> True")
#     else:
#         print(f"{num} -> False")


number = int(input())
for current_number in range (1, number+1):
    current_number_as_string = str(current_number)
    digits_sum = 0
    for digit in range(current_number_as_string):
        digit += 1
    is_special = False
    if digits_sum == 5 or digits_sum == 7 or digits_sum == 11:
        is_special = True
    print(f'{current_number}-> {is_special} ')