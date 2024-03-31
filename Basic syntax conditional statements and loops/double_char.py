# while True:
#    string_input = input()
#    if string_input == "End":
#        break
#    if string_input != "SoftUni":
#        new_string = ''.join(char * 2 for char in string_input)
#        print(new_string)



while True:
    string_input = input()
    if string_input == "End":
        break
    if string_input != "SoftUni":
        new_string = string_input * 2
        print(new_string)