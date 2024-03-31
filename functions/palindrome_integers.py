
# def is_palindrome(number):
#     str_number = str(number)
#     return str_number == str_number[::-1]
# numbers_input = input().split(", ")
#
# palindrome_results = []
# for num in numbers_input:
#     is_palindrome_result = is_palindrome(int(num))
#     palindrome_results.append(is_palindrome_result)
# for i in range(len(numbers_input)):
#     print(f"{palindrome_results[i]}")


def is_palindrome(list):
    result =''
    for num in list:
        if str(num) == str(num)[::-1]:
            result += "True\n"
        else:
            result += 'False\n'
    return result
list_of_palindrome = list(map(int, input().split(', ')))
print(is_palindrome(list_of_palindrome))