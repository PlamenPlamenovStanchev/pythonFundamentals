# string = input()
# result = []
# i= 0
# while i < len(string):
#     current_char = string[i]
#     if current_char == ">":
#         strenght = int(string[i+1])
#         i += 2
#         while i < len(string) and strenght > 0:
#             if string == ">":
#                 break
#             i += 1
#             strenght -= 1
#     else:
#         result.append(current_char)
#         i += 1
# result_string = "".join(result)
# print(result_string)

some_string = input()
final_string = ""
strenght = 0
for index in range(len(some_string)):
    if strenght > 0 and some_string[index] != ">":
        strenght -= 1
    elif some_string[index] == ">":
        final_string += some_string[index]
        strenght += int(some_string[index +1])
    else:
        final_string += some_string[index]
print(final_string)