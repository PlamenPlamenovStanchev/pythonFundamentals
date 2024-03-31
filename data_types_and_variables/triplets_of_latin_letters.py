# number = int(input())
# for i in range(0, number):
#     for j in range(0, number):
#         for k in range(0, number):
#             print(f"{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}")

number = int(input())
for i in range(number):
    for j in range(number):
        for k in range(number):
            first_letter = chr(ord("a") + i)
            second_letter = chr(ord("a") + j)
            third_letter = chr(ord("a") + k)
            print(f"{first_letter}{second_letter}{third_letter}")