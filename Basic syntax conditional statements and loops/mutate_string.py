first_string = input()
second_string = input()
last_string = first_string
for character_index in range(len(first_string)):
    left_side = second_string[:character_index +1]
    right_side = first_string[character_index+1:]
    new_string = left_side + right_side
    if new_string != last_string:
        print(new_string)
        last_string = new_string