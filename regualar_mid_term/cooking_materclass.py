
# import math
#
# def calculate_cost(budget, students, flour_price, egg_price, apron_price):
#     total_aprons = math.ceil(students * 1.2)
#
#     flour_cost = (students - students // 5) * flour_price  # Every 5th package is free
#     egg_cost = students * 10 * egg_price
#     apron_cost = total_aprons * apron_price
#
#     total_cost = flour_cost + egg_cost + apron_cost
#
#     return total_cost
#
# def main():
#     budget = float(input())
#     students = int(input())
#     flour_price = float(input())
#     egg_price = float(input())
#     apron_price = float(input())
#
#     total_cost = calculate_cost(budget, students, flour_price, egg_price, apron_price)
#
#     if total_cost <= budget:
#         print(f"Items purchased for {total_cost:.2f}$.")
#     else:
#         needed_money = total_cost - budget
#         print(f"{needed_money:.2f}$ more needed.")
#
# if __name__ == "__main__":
#     main()


import math

budget = float(input())
students = int(input())
price_flour = float(input())
price_egg = float(input())
price_apron = float(input())


flour_cost = (students - (students // 5)) * price_flour
egg_cost = students * 10 * price_egg
apron_cost = math.ceil(1.2 * students) * price_apron

total_cost = flour_cost + egg_cost + apron_cost
if total_cost <= budget:
    print(f"Items purchased for {total_cost:.2f}$.")
else:
    needed_money = total_cost - budget
    print(f"{needed_money:.2f}$ more needed.")