# text = "hello"
# result = "".join(sorted(set(text)))
# print(result)


# text = "hello world"
# result = "".join(text[i] for i in range(len(text)-1, -1, -1))
# print(result)


text = "hello world"
result = "".join([char.upper() if char.islower() else char.lower() for char in text])
print(result)