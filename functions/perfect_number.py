def is_perfect_number(number):
    if number <= 0:
        return False

    divisors_sum = 0
    for num in range(1, number):
        if number % num == 0:
            divisors_sum += num

    return divisors_sum == number

number_input = int(input())
if is_perfect_number(number_input):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")


# def is_perfect_number(number):
#     divisor_sum = sum(divisor for divisior in range(1, number) if number % divisior == 0)
#
#     if divisor_sum == number:
#         return "We have a perfect number!"
#     else:
#         return "It's not so perfect."
#
# number = int(input())
# print(is_perfect_number(number))