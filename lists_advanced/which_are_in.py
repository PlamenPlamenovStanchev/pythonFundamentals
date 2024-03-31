# first_string = input().split(", ")
# second_string = input().split(", ")
# new_list = []
# new_list = [string1 for string1 in first_string if any(string1 in string2 for string2 in second_string)]
# print(new_list)


first_string = input().split(", ")
second_string = input().split(', ')
new_list = []
for first_element in first_string:
    for second_element in second_string:
        if first_element in second_element:
            new_list.append(first_element)
            break
print(new_list)