# def is_valid_password(password):
#     if not (6 <= len(password) <= 10):
#         print("Password must be between 6 and 10 characters")
#         return False
#     if not password.isalnum():
#         print("Password must consist only of letters and digits")
#         return False
#     digit_count = sum(c.isdigit() for c in password)
#     if digit_count < 2:
#         print("Password must have at least 2 digits")
#         return False
#     print("Password is valid")
#     return True
# password_input = input()
# is_valid_password(password_input)


def is_valid_password(password):
    errors = []
    if not (6 <= len(password) <= 10):
        errors.append("Password must be between 6 and 10 characters")
    if not password.isalnum():
        errors.append("Password must consist only of letters and digits")
    if sum(char.isdigit() for char in password) <2:
        errors.append("Password must have at least 2 digits")
    if errors:
        for error in errors:
            print(error)
    else:
         print("Password is valid")
password_input = input()
is_valid_password(password_input)

# import re
#
# class PasswordValidator:
#     def __init__(self, password):
#         self.password = password
#         self.errors = []
#     def is_valid(self):
#         self.check_lenght()
#         self.check_alphanumeric()
#         self.check_digit_count()
#
#         if self.errors:
#             return False
#         return True
#
#     def check_lenght(self):
#         if not (6 <= len(self.password) <= 10):
#             self.errors.append("Password must be between 6 and 10 characters")
#     def check_alphanumeric(self):
#         if not re.match("^[a-zA-Z0-9]+$", self.password):
#             self.errors.append("Password must consist only of letters and digits")
#     def check_digit_count(self):
#         if sum(char.isdigit() for char in self.password) < 2:
#             self.errors.append("Password must have at least 2 digits")
#
#
#     def get_errors(self):
#         return self.errors
#
#
# user_password = input()
# validator = PasswordValidator(user_password)
# if validator.is_valid():
#     print("Password is valid")
# else:
#     for error in validator.get_errors():
#           print(error)