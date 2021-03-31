import os, json
import collections
import abc

# Transportation Logistics delivery handling by different types of vehicles

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


class Transportation:

    def create_transport(self):
        pass


class LandTransportation:
    def create_transport(self):
        return Bus()


class WaterTransportation:
    def create_transport(self):
        return Boat()


class TransportFactory:
    def __init__(self, type_of_transport):
        transport = None
        if type_of_transport == 'Water':
            transport = WaterTransportation()
        if type_of_transport == 'Land':
            transport = LandTransportation()
        self.transport = transport.create_transport()

    def deliver(self):
        self.transport.deliver(4, 5)


if __name__ == "__main__":
    t = TransportFactory("Water")
    t.deliver()
