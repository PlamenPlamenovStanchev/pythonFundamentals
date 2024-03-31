

# def calculate_tax(car_type, years, kilometers):
#     if car_type == "family":
#         initial_tax = 50
#         tax_decline_per_year = 5
#         tax_increase_per_km = 12
#         traveled_kilometers = 3000
#     elif car_type == "heavyDuty":
#         initial_tax = 80
#         tax_decline_per_year = 8
#         tax_increase_per_km = 14
#         traveled_kilometers = 9000
#     elif car_type == "sports":
#         initial_tax = 100
#         tax_decline_per_year = 9
#         tax_increase_per_km = 18
#         traveled_kilometers = 2000
#     else:
#         print("Invalid car type.")
#
#     tax = initial_tax - (years * tax_decline_per_year) + (kilometers // traveled_kilometers * tax_increase_per_km)
#
#     return tax
#
# def main():
#     vehicles = input().split(">>")
#
#     total_tax_collected = 0
#
#     for vehicle_info in vehicles:
#         car_data = vehicle_info.split(" ")
#         if len(car_data) == 3:
#             car_type, years, kilometers = car_data
#             years = int(years)
#             kilometers = int(kilometers)
#
#             tax_to_pay = calculate_tax(car_type, years, kilometers)
#             total_tax_collected += tax_to_pay
#
#             print(f"A {car_type} car will pay {tax_to_pay:.2f} euros in taxes.")
#
#     print(f"The National Revenue Agency will collect {total_tax_collected:.2f} euros in taxes.")
#
# if __name__ == "__main__":
#     main()

vehicles = input().split(">>")

total_tax_collected = 0

for vehicle in vehicles:
    car_data = vehicle.split(" ")
    if len(car_data) == 3:
        car_type, years, kilometers = car_data
        years = int(years)
        kilometers = int(kilometers)

        if car_type == "family":
            initial_tax = 50
            tax_decline_per_year = 5
            tax_increase_per_km = 12
            traveled_kilometers = 3000
        elif car_type == "heavyDuty":
            initial_tax = 80
            tax_decline_per_year = 8
            tax_increase_per_km = 14
            traveled_kilometers = 9000
        elif car_type == "sports":
            initial_tax = 100
            tax_decline_per_year = 9
            tax_increase_per_km = 18
            traveled_kilometers = 2000
        else:
            print("Invalid car type.")
            continue

        tax_to_pay = initial_tax- (years * tax_decline_per_year) + (kilometers // traveled_kilometers * tax_increase_per_km)

        total_tax_collected += tax_to_pay

        print(f"A {car_type} car will pay {tax_to_pay:.2f} euros in taxes.")

print(f"The National Revenue Agency will collect {total_tax_collected:.2f} euros in taxes.")

