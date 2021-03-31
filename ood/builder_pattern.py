import os, json
import collections

import abc


# Building an individual car or ship from scratch

class Vehicle:
    def __init__(self):
        self._parts = []

    @property
    def parts(self):
        return self._parts

    @parts.setter
    def parts(self, value):
        self._parts.append(value)


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.type_of_vehicle = "Car"


class Ship(Vehicle):
    def __init__(self):
        super().__init__()
        self.type_of_vehicle = "Ship"


class Builder:
    @abc.abstractmethod
    def build(self):
        pass

    def add_engine(self):
        pass

    def add_shape(self):
        pass

    def add_seats(self):
        pass


class CarBuilder(Builder):

    def __init__(self):
        self.vehicle = Car()

    def build(self):
        return self.vehicle

    def add_engine(self):
        self.vehicle.parts = "Engine"

    def add_shape(self):
        self.vehicle.parts = "Car Shape"

    def add_seats(self):
        self.vehicle.parts = "4 seats"


class BoatBuilder(Builder):

    def __init__(self):
        self.vehicle = Ship()

    def build(self):
        return self.vehicle

    def add_engine(self):
        self.vehicle.parts = "Engine"

    def add_shape(self):
        self.vehicle.parts = "Ship Shape"

    def add_seats(self):
        self.vehicle.parts = "100 seats"


class Director:

    @classmethod
    def construct(cls, builder):
        builder.add_engine()
        builder.add_shape()
        builder.add_seats()
        return builder.build()


def main():

    cb = CarBuilder()
    vehicle = Director.construct(cb)
    print(vehicle.parts)


if __name__ == "__main__":
    main()
