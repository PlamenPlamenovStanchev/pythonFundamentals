n = int(input())
for _ in range (n):
    number = int(input())
    if number == 88:
        print("Hello")
    elif number == 86:
        print("How are you?")
    elif number != 88 and number != 86 and number < 88:
        print("GREAT!")
    else:
        print("Bye.")


#number_of_messages = int(input())
#for current_message in range(number_of_messages):
#    number = int(input())
#    message = ""
#    if number == 88:
#        message = "Hello"
#    elif number == 86:
#        message = "How are you?"
#    elif number < 88:
#        message = "GREAT!"
#   else: #elif number > 88
#        message = "Bye."
#    print(message)