text = input().split()
even_lenght_words = [word for word in text if len(word) % 2 == 0]
for word in even_lenght_words:
    print(word)
