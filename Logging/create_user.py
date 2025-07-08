import logging
import calculation

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")

file_handler = logging.FileHandler("user.log")

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class User:
    def __init__(self, name: str, lastname: str, age: int) -> None:
        self.username = name
        self.user_lastname = lastname
        self.user_age = age
        logger.info(f"user {self.username} was created")


user_1 = User(name="Saqo", lastname="Petrosyan", age=29)
