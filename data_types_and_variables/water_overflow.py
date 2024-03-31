number_of_lines = int(input())
total_litres = 0
for litres in range(number_of_lines):
    litres_poured = int(input())
    if total_litres + litres_poured <= 255:
        total_litres += litres_poured
    else:
        print("Insufficient capacity!")
print(total_litres)


# number_of_lines = int(input())
# tank_capacity = 255
# for line in range(number_of_lines):
#     liters_of_water = int(input())
#     if tank_capacity - liters_of_water < 0:
#         print("Insufficient capacity!")
#         continue
#     tank_capacity -= liters_of_water
# print(255 - tank_capacity)
