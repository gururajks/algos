import os, json
import collections

import os, json
import collections
import abc


# Transportation Logistics delivery handling by different families of vehicles, Land vs Water

class Vehicle:
    @abc.abstractmethod
    def deliver(self, a, b):
        pass


class Boat(Vehicle):
    def __init__(self):
        self.name = "Bus"

    def deliver(self, a, b):
        print(f"Boat   {a} -> {b}")


class Bus(Vehicle):
    def __init__(self):
        self.name = "Bus"

    def deliver(self, a, b):
        print(f"Bus   {a} -> {b}")


class Car(Vehicle):
    def __init__(self):
        self.name = "Bus"

    def deliver(self, a, b):
        print(f"Car   {a} -> {b}")


class Ship(Vehicle):
    def __init__(self):
        self.name = "Bus"

    def deliver(self, a, b):
        print(f"Ship   {a} -> {b}")


class Destroyer(Vehicle):
    def __init__(self):
        self.name = "Bus"

    def deliver(self, a, b):
        print(f"Destroyer   {a} -> {b}")


class TransportationFactory:

    def __init__(self, type_of_transport):
        self.type_of_transport = type_of_transport

    def create_transport(self):
        pass


class LandTransportationFactory(TransportationFactory):

    def create_transport(self):
        if self.type_of_transport == 'Bus':
            return Bus()
        if self.type_of_transport == 'Car':
            return Car()


class WaterTransportationFactory(TransportationFactory):
    def create_transport(self):
        if self.type_of_transport == 'Ship':
            return Ship()
        if self.type_of_transport == 'Navy':
            return Destroyer()


class TransportFactory:
    def __init__(self, type_of_transport, type_of_vehicle):
        self.transport = None
        if type_of_transport == 'Water':
            self.transport = WaterTransportationFactory(type_of_vehicle)
        if type_of_transport == 'Land':
            self.transport = LandTransportationFactory(type_of_vehicle)
        self.transport = self.transport.create_transport()

    def deliver(self):
        self.transport.deliver(4, 5)


if __name__ == "__main__":
    t = TransportFactory("Water", "Destroyer")
    t.deliver()
