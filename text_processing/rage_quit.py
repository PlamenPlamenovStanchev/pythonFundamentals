text_input = input()
rage_massage = ""
repetitions = ""
sub_string = ""
for index in range(len(text_input)):
    if not text_input[index].isdigit():
        sub_string += text_input[index].upper()
    else:
        for next_symbol in range(index, len(text_input)):
            if not text_input[next_symbol].isdigit():
                break

            repetitions += text_input[next_symbol]
        rage_massage += sub_string * int(repetitions)
        repetitions = ""
        sub_string = ""
print(f"Unique symbols used: {len(set(rage_massage))}")
print(rage_massage)


