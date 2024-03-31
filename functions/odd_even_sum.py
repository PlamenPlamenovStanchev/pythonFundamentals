def sum_of_odd_and_even_digits(number):
    odd_sum = 0
    even_sum = 0

    for digit in str(number):
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    result_string = f"Odd sum = {odd_sum}, Even sum = {even_sum}"
    return result_string

number = int(input())
result = sum_of_odd_and_even_digits(number)
print(result)