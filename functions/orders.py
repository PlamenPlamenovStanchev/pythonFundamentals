product = input()
quantity = int(input())

def solve(quantity, product):
    total_price = None
    if product == "coffee":
        total_price = quantity * 1.50
    elif product == "water":
        total_price = quantity * 1.00
    elif product == "coke":
        total_price = quantity * 1.40
    elif product == "snacks":
        total_price = quantity * 2.00
    return total_price
print(solve(quantity, product))