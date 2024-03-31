import re

# year = input()
# regex = "\\b(?P<day>\\d{2})([-.\\/])(?P<month>[A-Z][a-z]{2})\\2(?P<year>\\d{4})\\b"
# matches = re.findall(regex, year)
# for match in matches:
#     print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")


year = input()
regex = r'(\d{2})([.-/])([A-Z][a-z]{2})\2(\d{4})'
matches = re.findall(regex, year)
for match in matches:
    day = match[0]
    separator = match[1]
    month = match[2]
    year = match[3]
    print(f"Day: {day} Month: {month} Year: {year}")
