from abc import abstractmethod, ABC
from enum import Enum


class VehicleType(Enum):
    BUS = 1
    CAR = 2


class Vehicle(ABC):
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    @abstractmethod
    def fuel_consumption(self):
        pass


class Bus(Vehicle):
    def __init__(self, brand, year):
        super().__init__(brand, year)

    def fuel_consumption(self) -> str:
        return "8 MPG"


class Car(Vehicle):
    def __init__(self, brand, year):
        super().__init__(brand, year)

    def fuel_consumption(self) -> str:
        return "24 MPG"


class VehicleFactory:
    def __init__(self, vehicle_type: VehicleType, brand, year) -> None:
        self.vehicle_type = vehicle_type
        self.brand = brand
        self.year = year

    def get_vehicle(self) -> Vehicle:
        if self.vehicle_type == VehicleType.BUS:
            return Bus(self.brand, self.year)
        elif self.vehicle_type == VehicleType.CAR:
            return Car(self.brand, self.year)
        else:
            raise ValueError(f"Unknown VehicleType supplied as argument: {self.vehicle_type}")


def main():
    my_car = VehicleFactory(VehicleType.CAR, "Ford", 1956).get_vehicle()
    my_bus = VehicleFactory(VehicleType.BUS, "Ford", 2022).get_vehicle()
    print(f'Car MPG: {my_car.fuel_consumption()} Bus MPG: {my_bus.fuel_consumption()}')


if __name__ == '__main__':
    main()
