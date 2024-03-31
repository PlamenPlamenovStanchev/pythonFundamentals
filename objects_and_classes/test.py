# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
#
#     def deposit(self, amount):
#         self.__balance += amount
#
#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             return amount
#         else:
#             return "Insufficient funds"
#
# account = BankAccount(1000)
# account.deposit(500)
# print(account.withdraw(2000))


class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise ValueError("Name must be a string")