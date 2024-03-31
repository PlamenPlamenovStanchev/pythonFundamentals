tail = input()
head = input()
body = input()
meercats = [tail, head, body]
meercats[0], meercats[1],meercats[2] = meercats[1], meercats[2], meercats[0]
print(meercats)