devisor = int(input())
boundry = int(input())
for number in range(boundry, devisor - 1, -1):
    if number % devisor == 0:
        break
print(number)
