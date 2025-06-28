
"""
Demonstrates Python name mangling with double underscore attributes in a class.

This script defines a BankAccount class with a private __id attribute,
showing how name mangling prevents direct access to the attribute from outside the class.
"""
from uuid import uuid4

class BankAccount:
    """
    A simple bank account class demonstrating name mangling for private attributes.

    Attributes:
        name (str): The account holder's first name.
        surname (str): The account holder's surname.
        age (int): The account holder's age.
        __id (UUID): A unique identifier for the account (private).
    """
    def __init__(self, name: str, surname: str, age: int):
        """
        Initializes a new BankAccount instance with the given name, surname, and age.
        Generates a unique private ID for the account.
        """
        self.name = name
        self.surname = surname
        self.age = age
        self.__id = uuid4()
    def show_id(self):
        """
        Prints the private account ID.
        """
        print(self.__id)
account = BankAccount(name='Sargis', surname='Petrosyan', age=29)
account.show_id()
print(account.__id) # ---> will raise error
