
numbers_input = input().split()
n = int(input())
numbers = list(map(int, numbers_input))
for _ in range(n):
    if numbers:
        numbers.remove(min(numbers))
print(", ".join(map(str, numbers)))