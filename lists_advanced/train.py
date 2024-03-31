train_lenght = int(input())
train = [0]*train_lenght
command = input()
while command != "End":
    tokens = command.split()
    key_word = tokens[0]
    if key_word == "add":
        people = int(command[1])
        train[-1] += people

    elif key_word == "insert":
        index = int(command[1])
        people = int(command[2])
        train[index] += people

    elif key_word == "leave":
        index = int(command[1])
        people = int(command[2])
        train[index] -= people

    print(train)
