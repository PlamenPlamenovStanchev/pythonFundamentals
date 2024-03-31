# text = input()
# encrypted_text = ""
# for char in text:
#     if char.isalpha():
#         base = ord("A") if char.isupper() else ord("a")
#         encrypted_char = chr((ord(char) - base + 3) % 26 + base)
#         encrypted_text += encrypted_char
#     else:
#         encrypted_text += char
# print(encrypted_text)



text = input()
encrypted_text = ""
for character in text:
    encrypted_character = chr(ord(character)+3)
    encrypted_text += encrypted_character
print(encrypted_text)

