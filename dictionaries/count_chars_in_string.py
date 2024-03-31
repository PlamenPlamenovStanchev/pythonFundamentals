# string = input()
# char_count = {}
# for char in string:
#     if char != " ":
#         char_count[char] = char_count.get(char, 0) + 1
# for char, occurrences in char_count.items():
#     print(f"{char} -> {occurrences}")



def count_letters(current_text):
    chars_dict = {}
    for word in current_text:
        for letter in word:
            if letter not in chars_dict:
                chars_dict[letter] = 1
            else:
                chars_dict[letter] += 1
    return chars_dict
text = input().split()
characters_dictionary = count_letters(text)
for k, v in characters_dictionary.items():
    print(f" {k} -> {v}")
