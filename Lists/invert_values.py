# string = input()
# numbers = list(map(int, string.split()))
# opposites = [-num for num in numbers]
# print(opposites)

string = input().split()
opposites = []
for element in string:
    opposite_number = -int(element)
    opposites.append(opposite_number)
print(opposites)