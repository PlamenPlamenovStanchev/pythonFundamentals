# secret_message = input().split()
# decoded_words = []
# for word in secret_message:
#     first_letter = int(word[:-1])
#     deciphered_word = chr(first_letter) + word[-1] + word[2:-1] + word[1]
#     decoded_words.append(deciphered_word)
# decode_message = " ".join(decoded_words)
# print("Deciphered message:", decode_message)

# Input: Receive the secret message as a string of words
# secret_message = input()

# Process each word in the secret message and decipher
# decoded_words = []
# for word in secret_message.split():
#     first_letter_code = int(word[:-1])
#     deciphered_word = chr(first_letter_code) + word[-1] + word[2:-1] + word[1]
#     decoded_words.append(deciphered_word)

# Output: Print the deciphered message
# decoded_message = ' '.join(decoded_words)
# print("Deciphered Message:", decoded_message)


secret_message = input().split()
for message in secret_message:
    numbers_list = [digit for digit in message if digit.isdigit()]
    number = int(''.join(numbers_list))
    character = chr(number)
    message_without_digits = [char for char in message if not char.isdigit()]
    message_without_digits.insert(0,character)
    message_without_digits[1], message_without_digits[-1] = message_without_digits[-1], message_without_digits[1]
    filtered_message = ''.join(message_without_digits)
    print(filtered_message, end=' ')
