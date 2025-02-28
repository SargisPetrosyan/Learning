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
    """
    The Factory Pattern provides a way to create objects without specifying the exact class of object 
    that will be created. It defines an interface for creating objects, but allows subclasses to 
    alter the type of objects that will be created.

    Why use it?
    - Allows for easy creation of objects while abstracting the instantiation process.
    - Useful when the exact type of object to be created is determined at runtime.
    - Helps in reducing tight coupling by allowing the client code to rely on a factory to create objects.
    """
    
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
