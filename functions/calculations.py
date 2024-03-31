operator = input()
first_number = int(input())
second_number = int(input())
def solve(first_number, second_number, operator):
    result = None
    if operator == "multiply":
        result = first_number * second_number
    elif operator == "devide":
        result = first_number // second_number
    elif operator == "add":
        result = first_number + second_number
    elif operator == "subtract":
        result = first_number - second_number
    return result
print(solve(first_number, second_number, operator))