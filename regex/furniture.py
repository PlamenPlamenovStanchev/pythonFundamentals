# total_cost = 0
# furniture = []
# while True:
#     command = input()
#     if command == "Purchase":
#         break
#     start_index = command.find(">>")
#     end_index = command.find("<<")
#     furniture_name = command[start_index + 2: end_index]
#
#     start_index = command.find("!")
#     end_index = len(command)
#     price_quantity = command[start_index + 1: end_index].split("!")
#     price = float(price_quantity[0])
#     quantity = int(price_quantity[1])
#     total_cost += price * quantity
#     furniture.append(furniture_name)
# print("Bought furniture:")
# for name in furniture:
#     print(name)
# print(f"Total money spend: {total_cost:.2f}")

# total_cost = 0.0
# furniture = {}
#
# while True:
#     line = input()
#     if line == "Purchase":
#         break
#
#     name, price, quantity = line.strip("!><").split("<<")
#     price = float(price)
#     quantity = int(quantity)
#
#     if name not in furniture:
#         furniture[name] = price * quantity
#     else:
#         furniture[name] += price * quantity
#         total_cost -= price * quantity
#
#     total_cost += price * quantity
#
# print("Bought furniture:")
# for name, price in furniture.items():
#     print(name)
#
# print("Total money spend: {:.2f}".format(total_cost))

import re
bought_furniture = []
total_cost = 0
pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'
command = input()
while command != "Purchase":
    matches = re.search(pattern, command)
    if matches:
        furniture, price, quantity = matches.groups()
        bought_furniture.append(furniture)
        total_cost += float(price)*int(quantity)
    command = input()
print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_cost:.2f}")
