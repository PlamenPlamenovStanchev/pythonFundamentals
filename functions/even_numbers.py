numbers = input().split()
even_numbers = list(map(int, filter(lambda x: int(x) % 2 == 0, numbers)))
print(even_numbers)



