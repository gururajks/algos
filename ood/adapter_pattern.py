import os, json
import collections

# Tow truck tows a car
# If a boat is attached it can fail
# BUT WHAT IF YOU USE AN ADAPTER SO THAT TOW TRUCK CAN EASILY CONNECT

class Vehicle:
    def __init__(self):
        pass


class Car(Vehicle):
    def __init__(self):
        print("Car created")

    def weight(self):
        return "100kg"


class Boat(Vehicle):
    def __init__(self):
        print("Boat created")

    def weight(self):
        return "1000 kg"


class TowTruck:
    def tow(self, car):
        print("weight:" + car.weight())


class Adapter(Car):
    def __init__(self, boat):
        self.boat = boat

    def weight(self):
        return self.boat.weight()


if __name__ == "__main__":

    t = TowTruck()
    c = Car()
    t.tow(c)

    # create a boat and add an adapter
    # so that Towtruck doesnt know its towing a boat
    b = Boat()
    adapter = Adapter(b)
    t.tow(adapter)
