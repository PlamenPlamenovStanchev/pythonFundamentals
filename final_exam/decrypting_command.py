string = input()
while True:
    command = input()
    if command == "Finish":
        break
    current_command = command.split()
    if len(current_command) < 2:
        continue
    action = current_command[0]
    if action == "Replace":
        current_char = current_command[1]
        new_char = current_command[2]
        string = string.replace(current_char, new_char)
        print(string)
    elif action == "Cut":
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        if start_index < 0 or end_index >= len(string) or start_index > end_index:
            print("Invalid indices!")
            continue
        string = string[:start_index] + string[end_index+1:]
        print(string)
    elif action == "Make":
        case = current_command[1]
        if case == "Upper":
            string = string.upper()
        elif case == "Lower":
            string = string.lower()
        print(string)
    # elif command[0] == "Check":
    #     string_to_check = command[1]
    #     if string_to_check in string:
    #         print(f"Message contains {string_to_check}")
    #     else:
    #         print(f"Message doesn't contain {string_to_check}")
    elif action == "Check":
        string_to_check = current_command[1]
        if string.find(string) != -1:
            print("Message doesn't contain " + string_to_check)
        else:
            print("Message contains " + string_to_check)

    elif action == "Sum":
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        if start_index < 0 or end_index >= len(string) or start_index > end_index:
            print("Invalid indices!")
            continue
        substring = string[start_index:end_index + 1]
        print(sum(map(ord, substring)))
