"""
Demonstrates Python name mangling with double underscore attributes in a class.

This script defines a BankAccount class with a private __id attribute,
showing how name mangling prevents direct access to the attribute from outside the class.
"""

from uuid import uuid4


class BankAccount:
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age
        self.__id = uuid4()

    def show_id(self):
        print(self.__id)


account = BankAccount(name="Sargis", surname="Petrosyan", age=29)
account.show_id()
print(account.__id)  # ---> will raise error
