import os, json
import collections
import random


# flyweight pattern helps in reducing memory consumption by storing the external properties that dont change
# when creating the actual object, use these cached property directly without having to store them in the individual
# properties

class VehicleProperty:
    def __init__(self, color, hp, type_of_vehicle):
        self.color = color
        self.hp = hp
        self.type_of_vehicle = type_of_vehicle

    def race(self, x, y):
        print(
            f"{self.color} vehicle with {self.hp} racing in the {self.type_of_vehicle} group and is in {x}:{y} position")


class VehicleRegistry:

    def __init__(self):
        self.cache = {}

    def find_vehicle(self, vehicle_type):
        return self.cache.get(vehicle_type)

    def add_vehicle(self, vehicle_type, color, hp, type_of_vehicle):
        self.cache[vehicle_type] = VehicleProperty(color, hp, type_of_vehicle)


class Vehicle:
    def __init__(self, vehicle_prop):
        self.vehicleProp = vehicle_prop
        self.x = 0
        self.y = 0

    def move(self):
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        self.vehicleProp.race(x, y)


class Game:
    def __init__(self):
        self.vehicle_registry = VehicleRegistry()

    def register(self, vehicle_prop, color, hp, type_of_vehicle):
        self.vehicle_registry.add_vehicle(vehicle_prop, color, hp, type_of_vehicle)

    def race(self, vehicle_prop):
        vehicle_prop = self.vehicle_registry.find_vehicle(vehicle_prop)
        v = Vehicle(vehicle_prop)
        v.move()


def main():
    g = Game()
    g.register("Reddy", "Red", 100, "Porche")
    g.register("Blue Manga", "Blue", 100, "Porche")
    g.register("Red Baron", "Red", 1000, "Lamborghini")

    g.race("Red Baron")
    g.race("Blue Manga")


if __name__ == "__main__":
    main()
