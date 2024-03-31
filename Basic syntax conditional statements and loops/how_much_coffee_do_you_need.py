coffees_needed = 0
while True:
    event = input()
    if event == "END":
        break
    if event == "coding":
        coffees_needed += 1
    elif event == "CODING":
        coffees_needed += 2
    elif event == "dog" or event == "cat":
        coffees_needed += 1
    elif event == "DOG" or event == "CAT":
        coffees_needed +=2
    elif event == "movie":
        coffees_needed += 1
    elif event == "MOVIE":
        coffees_needed += 2
    else:
        continue
if coffees_needed <= 5:
    print(coffees_needed)
else:
    print("You need extra sleep")