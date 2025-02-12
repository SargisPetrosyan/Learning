from abc import ABC

"""Polimorphism is using same function for handle differnet purpose"""


class Vehicle(ABC):
    @classmethod
    def drive(self, car_model: str) -> None: ...


class BMW(Vehicle):
    def drive(self, car_model: str) -> None:
        print(f"BMW model:{car_model} is driving!!!")


class Mercedes(Vehicle):
    def drive(self, car_model: str) -> None:
        print(f"Mercedes model:{car_model} is driving!!!")


class Volvo(Vehicle):
    def drive(self, car_model: str) -> None:
        print(f"Volvo model{car_model} is driving!!!")


def buy_car(car_model: Vehicle, model: str):
    car_model.drive(model)


bmw: BMW = BMW()
mercedes: Mercedes = Mercedes()
volvo: Volvo = Volvo()

buy_car(car_model=bmw, model="m3")
buy_car(car_model=mercedes, model="s200")
