string = input()
digits = ""
letters = ""
others = ""
for ch in string:
    if ch.isdigit():
        digits += ch
    elif ch.isalpha():
        letters += ch
    else:
        others += ch
print(digits)
print(letters)
print(others)