# number_string = input().split(", ")
# numbers_list = [int(num) for num in number_string]
# positive_numbers_list = [str(num) for num in numbers_list if num >= 0]
# negative_numbers_list = [str(num) for num in numbers_list if num < 0]
# even_numbers_list = [str(num) for num in numbers_list if num % 2 == 0]
# odd_numbers_list = [str(num) for num in numbers_list if num % 2 != 0]
# print("Positive:", ", ".join(positive_numbers_list))
# print("Negative:", ", ".join(negative_numbers_list))
# print("Even:", ", ".join(even_numbers_list))
# print("Odd:", ", ".join(odd_numbers_list))


def positive_numbers(list_of_number):
    return ', '.join([number for number in list_of_number if number >= 0])

def negative_numbers(list_of_number):
    return ", ".join([number for number in list_of_number if number < 0])

def even_numbers(list_of_numbers):
    return ", ".join([number for number in list_of_numbers if number % 2 == 0])

def odd_numbers(list_of_number):
    return ", ".join([number for number in list_of_number if number % 2 != 0])

numbers = input().split(", ")
print(f"Positive: {positive_numbers(numbers)}")
print(f"Negative: {negative_numbers(numbers)}")
print(f"Even: {even_numbers(numbers)}")
print(f"Odd: {odd_numbers(numbers)}")




