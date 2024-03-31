# usernames = input().split(", ")
# valid_usernames = [username for username in usernames if 3 <= len(username) <= 16 and all(char.isalnum() or char in ['-', '_'] for char in username)]
# for valid_username in valid_usernames:
#     print(valid_username)



def lenght_is_valid(name):
    if 3 <= len(name) <= 16:
        return True
    return False

def charackters_are_valid(name):
    for charackter in name:
        if not (charackter.isalnum() or charackter == "-" or charackter == "_"):
            return False
    return True

def redundent_symbols(name):
    if ' ' in name:
        return False
    return True

def username_is_valid(name):
    if lenght_is_valid(name) and charackters_are_valid(name) and redundent_symbols(name):
        return True
    return False

usernames = input().split(", ")
for username in usernames:
    if username_is_valid(username):
        print(username)



