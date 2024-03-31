num1 = int(input())
num2 = int(input())
num3 = int(input())

def smallest(num1, num2, num3):
    smallest_number = min(num1, num2, num3)
    return smallest_number
print(smallest(num1, num2, num3))