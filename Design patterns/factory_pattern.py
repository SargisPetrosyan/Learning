from abc import ABC, staticmethod


# Vehicle abstract class
class Vehicle(ABC):
    @staticmethod
    def model():
        pass


class Car(Vehicle):
    def __init__(self) -> None:
        self.name = "Car"

    def model(self) -> str:
        return "BMW"


class Motorbike(Vehicle):
    def __init__(self) -> None:
        self.name = "Motorbike"

    def model(self) -> str:
        return "Mercedes"


class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type: str) -> Vehicle:
        vehicles = {"Car": Car, "Motorbike": Motorbike}
        if vehicle_type in vehicles:
            return vehicles[vehicle_type]()
        else:
            raise ValueError(f"Unknown vehicles {vehicle_type}")


if __name__ == "__main__":
    choice = input("What type of vehicle do you want to create? ")
    try:
        vehicle = VehicleFactory.create_vehicle(choice)
        print(f"Created a {vehicle.name}, Model: {vehicle.model()}")
    except ValueError as e:
        print(e)
