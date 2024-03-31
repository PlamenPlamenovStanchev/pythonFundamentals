# string1, string2 = input().split()
# total_sum = 0
# for char1, char2 in zip(string1, string2):
#     total_sum += ord(char1) * ord(char2)
#
# total_sum += sum(ord(char) for char in string1[len(string2):]) + sum(ord(char) for char in string2[len(string1):])
# print(total_sum)


first_string, second_string = input().split()
total_sum = 0
if len(first_string) > len(second_string):
    for index in range(len(second_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(second_string), len(first_string)):
        total_sum += ord(first_string[index])
elif len(second_string) > len(first_string):
    for index in range(first_string):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(first_string), len(second_string)):
        total_sum += ord(second_string[index])
else:
    for index in range(len(second_string)):
        total_sum += ord(first_string[index]) * ord(second_string[second_string])
print(total_sum)