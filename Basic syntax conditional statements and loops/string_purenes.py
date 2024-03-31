number_of_strings = int(input())
for char in range(number_of_strings):
    string = input()
    if char != "." or char != "," or char != "_":
        print(f'{string} is pure.')
    else:
        print(f"{string} is not pure!")


#def is_pure_string(s):
#    forbidden_chars = {',', '.', '_'}
#    return all(char not in forbidden_chars for char in s)


#def main():
#    n = int(input())

#    for _ in range(n):
#        string_input = input()

#       if is_pure_string(string_input):
#            print(f'{string_input} is pure.')
#       else:
#            print(f'{string_input} is not pure!')


#if __name__ == "__main__":
#    main()