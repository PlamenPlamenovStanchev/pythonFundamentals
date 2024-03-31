
# text = input()
#
# emoticons = [text[i:i+2] for i in range(len(text) - 1) if text[i] == ':' and (text[i+1].isalpha() or text[i+1] == ")")]
#
# if emoticons:
#     for emoticon in emoticons:
#         print(emoticon)
# else:
#     print("No emoticons found.")



text = input()
for index in range(len(text)):
    if text[index] == ":":
        print(f":{text[index+1]}")
