num1 = int(input())
num2 = int(input())
num3 = int(input())

def sum_numbers(num1, num2):
    sum = num1 + num2
    return sum

def subtract(sum, num3):
    sub = sum - num3
    return sub

def add_and_subtrack(num1, num2, num3):
    sum = sum_numbers(num1, num2)
    sub = subtract(sum, num3)
    return sub

print(add_and_subtrack(num1, num2, num3))

