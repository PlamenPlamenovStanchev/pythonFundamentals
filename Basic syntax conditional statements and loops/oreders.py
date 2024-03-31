number_of_orders = int(input())
total_price = 0
for current_order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsule_needed_per_day = int(input())
    if 0 < price_per_capsule > 100 \
            or 1 < days > 31 \
            or 0 < capsule_needed_per_day > 2000:
        continue
    price = price_per_capsule * days * capsule_needed_per_day
    total_price =+ price
    print(f'The price for the coffee is: ${price:.2f}')
print(f'Total: ${total_price:.2f}')

#number_of_orders = int(input())
#total_price = 0
#for order in range(number_of_orders):
#    price_per_capsule = float(input())
#    days = int(input())
#   capsules_per_day = int(input())
#    if price_per_capsule < 0.01 or price_per_capsule > 100.00:
#        continue
#    elif days not in range(1, 31 + 1):
#        continue
#    elif capsules_per_day not in range(1, 2000 + 1):
#        continue
#    price = days * capsules_per_day * price_per_capsule
#    total_price += price
#    print(f"The price for the coffee is: ${price:.2f}")
#print(f"Total: ${total_price:.2f}")