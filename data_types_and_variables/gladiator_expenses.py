# number_of_losts = int(input())
# shield_price = float(input())
# sword_price = float(input())
# helmet_price = float(input())
# armour_price = float(input())
#
# total_price = 0
# shield_breaks = 0
# for current_lost in range(1, number_of_losts + 1):
#     if current_lost % 2 == 0:
#         total_price += helmet_price
#     if current_lost % 3 == 0:
#         total_price += sword_price
#     if current_lost % 6 == 0:
#         total_price += shield_price
#         shield_breaks += 1
#         if shield_breaks % 2 == 0:
#             total_price += armour_price
# print(f"Gladiator expenses: {total_price:.2f} aureus")


number_of_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armour_price = float(input())

total_helmet_broken = number_of_lost_fights // 2
total_sword_broken = number_of_lost_fights // 3
total_shield_broken = number_of_lost_fights // (2 * 3)
total_armour_broken = total_shield_broken // 2
total_sum = total_helmet_broken * helmet_price\
            + total_sword_broken * sword_price\
            + total_shield_broken * shield_price\
            + total_armour_broken * armour_price
print(f'Gladiator expenses: {total_sum:.2f} aureus')
