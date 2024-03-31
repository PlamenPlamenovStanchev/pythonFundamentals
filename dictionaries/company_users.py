# companies = {}
#
# while True:
#     line = input()
#     if line == "End":
#         break
#
#     company, employee_id = line.split(" -> ")
#
#     if company not in companies:
#         companies[company] = []
#
#     companies[company].append(employee_id)
#
# for company, employees in companies.items():
#     print(company)
#     for employee_id in employees:
#         print(f"-- {employee_id}")

companies = {}
while True:
    command = input()
    if command == "End":
        break
    company, employee_id = command.split(" -> ")

    if company not in companies:
        companies[company] = []
    companies[company].append(employee_id)
for company, employees in companies.items():
    print(company)
    for employee_id in employees:
        print(f"--{employee_id}")

# companies = {}
# while True:
#     command = input()
#     if command == "End":
#         break
#     company, employee_id = command.split(" -> ")
#
#     if company not in companies:
#         companies[company] = [employee_id]
#     companies[company].append(employee_id) if employee_id not in companies[company] else...
# for company, employees in companies.items():
#     print(company)
#     for employee_id in employees:
#         print(f"--{employee_id}")