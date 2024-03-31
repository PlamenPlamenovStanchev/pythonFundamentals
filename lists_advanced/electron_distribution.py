number_of_electrons = int(input())
filled_shells = []
shell_position = 1
while number_of_electrons > 0:
    max_electrons_in_a_shell = 2 * (shell_position ** 2)
    if number_of_electrons >= max_electrons_in_a_shell:
        filled_shells.append(max_electrons_in_a_shell)
        number_of_electrons -= max_electrons_in_a_shell
    else:
        filled_shells.append(number_of_electrons)
        number_of_electrons = 0
    shell_position += 1
print(filled_shells)