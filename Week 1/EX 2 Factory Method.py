from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car is ready to drive")

class Truck(Vehicle):
    def start(self):
        print("Truck is ready to transport")

class VehicleFactory:
    def create_vehicle(self, vehicle_type):
        if vehicle_type.lower() == "car":
            return Car()
        elif vehicle_type.lower() == "truck":
            return Truck()
        else:
            raise ValueError("Invalid vehicle type")

factory = VehicleFactory()

car = factory.create_vehicle("car")
car.start()

truck = factory.create_vehicle("truck")
truck.start()