# char1 = input()
# char2 = input()
#
# def characters_in_between(char1, char2):
#     start_char = min(char1, char2)
#     end_char = max(char1, char2)
#     result_string = ""
#     for symbol in range(ord(start_char)+1, ord(end_char)):
#         result_string += chr(symbol) + ""
#         return result_string.rstrip()
#
# result = characters_in_between(char1, char2)
# print(result)


#
# def characters_in_between(char1, char2):
#     start_char = min(char1, char2)
#     end_char = max(char1, char2)
#
#     result_string = ""
#
#     for char_code in range(ord(start_char) + 1, ord(end_char)):
#         result_string += chr(char_code) + " "
#
#     return result_string.rstrip()
#
# char1 = input()
# char2 = input()
# result = characters_in_between(char1, char2)
# print(result)

def character_in_range(first_char, second_char):
    result = " "
    for i in range(ord(first_char)+1, ord(second_char)):
        result += chr(i) + " "
    return result

char1 = input()
char2 = input()
print(character_in_range(char1, char2))


# chars_in_range = lambda first_char, second_char: " ".join(map(chr, range(ord(first_char) + 1, ord(second_char))))
# char1 = input()
# char2 = input()
# print(chars_in_range(char1, char2))