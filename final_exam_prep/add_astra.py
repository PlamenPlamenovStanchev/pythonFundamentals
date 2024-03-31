import re

information = input()
pattern = r"(?i)([#|])([a-z\s])\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
matches = re.findall(pattern, information)
total_calories = sum([int(match[3])for match in matches])
for match in matches:
    item_name = match[1]
    expiration_date = match[2]
    calories = match[3]
    print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")
    