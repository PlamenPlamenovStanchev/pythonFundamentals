notes = [0]*10
while True:
    command = input()
    if command == "End":
        break
    tokens = command.split("-")
    priority = int(command[0])-1
    note = tokens[1]
    notes.pop(priority)
    notes.index(priority,note)
result = [element for element in notes if element !=0]
print(result)
