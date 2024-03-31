def factorial(number):
    if number == 0:
        return 1
    else:
        result = number * factorial(number - 1)
        return result

def factorial_devision(num1, num2):
    result_1 = factorial(num1)
    result_2 = factorial(num2)
    devision_result = result_1 /result_2
    return f"{devision_result:.2f}"

first_number = int(input())
second_number = int(input())
print(factorial_devision(first_number, second_number))

