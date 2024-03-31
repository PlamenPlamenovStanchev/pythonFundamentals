# string = input()
# result_string = ""
# for i in range(len(string)):
#     if i == 0 or string[i] != string[i-1]:
#         result_string += string[i]
# print(result_string)


text = input()
final_text = ""
last_added_character = ""
for current_character in text:
    if current_character != last_added_character:
        final_text += current_character
        last_added_character = current_character
print(final_text)
