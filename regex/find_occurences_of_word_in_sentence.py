# import re
# sentence = input()
# word = input()
# word = word.lower()
# sentence = sentence.lower()
# regex = r'\b' + word + '\b'
# matches = re.findall(regex, sentence)
# count = sentence.lower().count(word)
# print(count)


# def count_word_occurrences(string, word):
#     string_lower = string.lower()
#     word_lower = word.lower()
#     count = string_lower.count(word_lower)
#     return count
#
# string = input()
# word = input()
# result = count_word_occurrences(string, word)
# print(result)

import re
sentence = input()
searched_word = input()
pattern = fr'(?i)\b{searched_word}\b'
matches = re.findall(pattern, sentence)
# matches = re.findall(pattern, sentence, re.IGNORCASE)
print(len(matches))