import re

n = int(input())
for _ in range(n):
    password = input()
    pattern = r"^([^<>]+)>(\d+)\|([a-z]+)\|([A-Z]+)\|([^<>]+)<\1$"
    match = re.match(pattern, password)
    if match:
        encrypted_password = match.group(2)+match.group(3)+match.group(4)+match.group(5)
        print(f"Password: {encrypted_password}")
    else:
        print("Try another password!")