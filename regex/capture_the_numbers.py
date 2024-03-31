# import re
# numbers = []
# while True:
#     text = input()
#     if not text:
#         break
#     number_of_matches = re.findall(r'\d+', text)
#     numbers.extend(number_of_matches)
# print(" ".join(numbers))


import re

line = input()
while line:

    pattern = r'\d+'
    matches = re.findall(pattern, line)
    if matches:
        print(" ".join(matches), end=" ")
    line = input()
