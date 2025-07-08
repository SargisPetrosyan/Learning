import logging
import logging.config

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")

file_handler = logging.FileHandler("calculator.log")
file_handler.setLevel(logging.ERROR)

file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def add(x: int | float, y: int | float):
    return x + y


def subtract(x: int | float, y: int | float):
    return x - y


def multiply(x: int | float, y: int | float):
    return x * y


def divide(x: int | float, y: int | float):
    try:
        result = x / y
    except ZeroDivisionError:
        logger.error("tyred by divide by 0")
    else:
        return result


x = 30
y = 0

add_result = add(x=x, y=y)
logger.debug(f"add_result: {add_result}")

subtract_result = subtract(x=x, y=y)
logger.debug(f"subtract_result: {subtract_result}")

multiply_result = multiply(x=x, y=y)
logger.debug(f"multiply_result: {multiply_result}")

divide_result = divide(x=x, y=y)
logger.debug(f"divide_result: {divide_result}")


# logging types
#
# debug()
# info()
# warning()
# error()
# critical()
