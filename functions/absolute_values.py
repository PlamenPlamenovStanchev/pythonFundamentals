# strings = input().split()
# list_of_numbers =[]
# for num in strings:
#     number = float(num)
#     list_of_numbers.append(number)
# list_of_absolute_numbers = []
# for num in list_of_numbers:
#     absolute_number = abs(num)
#     list_of_absolute_numbers.append(absolute_number)
# print(list_of_absolute_numbers)

string_of_numbers = input().split()
absolute_numbers = []

for number in string_of_numbers:
    absolute_numbers.append(abs(float(number)))
print(absolute_numbers)