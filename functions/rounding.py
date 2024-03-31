# strings_of_numbers = input().split()
# list_of_numbers =[]
# for num in strings_of_numbers:
#     number = float(num)
#     list_of_numbers.append(number)
# list_of_rounded_numbers = []
# for num in list_of_numbers:
#     rounded_number = round(num)
#     list_of_rounded_numbers.append(rounded_number)
# print(list_of_rounded_numbers)

string_of_numbers = input().split()
rounded_numbers = []

for number in string_of_numbers:
    rounded_numbers.append(round(float(number)))
print(rounded_numbers)