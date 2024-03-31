import math
number_people = int(input())
elevator_capacity = int(input())
cources = math.ceil(number_people / elevator_capacity)
print(cources)