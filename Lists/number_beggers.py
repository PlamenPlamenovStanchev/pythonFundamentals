
# numbers_input = input()
# beggars_count = int(input())
#
# numbers = list(map(int, numbers_input.split(', ')))
# beggars_sums = [0] * beggars_count
#
# for i, num in enumerate(numbers):
#     beggar_index = i % beggars_count
#     beggars_sums[beggar_index] += num
#
# print(beggars_sums)


strings_of_integers = input().split(", ")
count_of_beggars = int(input())
money_as_integer =[]
for integer in strings_of_integers:
    money_as_integer.append(int(integer))
final_sum = []
start_index = 0
for current_beggar in range(count_of_beggars):
    current_beggar_sum = 0
    for current_index in range(start_index, len(money_as_integer), count_of_beggars):
        current_beggar_sum += money_as_integer[current_index]
    final_sum.append(current_beggar_sum)
    start_index += 1
print(final_sum)