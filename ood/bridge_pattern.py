import os, json
import collections


# Use a bridge pattern when you want an interface to control the composition classes
# Here we have engine and a car bridge.
# Tesla has an electric engine, to create and upgrade, we use a common implementation (bridge pattern) to
# control upgrade of the car


class Engine:
    def __init__(self):
        print("Engine created")
        self.type_of_engine = ""

    def upgrade(self):
        print(self.type_of_engine + " upgraded")


class Gas(Engine):
    def __init__(self):
        self.type_of_engine = "Gas"
        print("Gas Engine created")
        self.curr_mileage = "20miles/gallon"


class Electric(Engine):
    def __init__(self):
        self.type_of_engine = "Electric"
        print("Electric Engine created")
        self.curr_mileage = "400miles/charge"


class Hybrid(Engine):
    def __init__(self):
        self.type_of_engine = "Hybrid"
        print("Hybrid Engine created")
        self.curr_mileage = "50miles/gallon"


class CarBridge:
    def __init__(self, engine):
        print("Car Created")
        self.engine = engine

    def stats(self):
        self.engine.upgrade()
        print(self.engine.curr_mileage)


class Tesla(CarBridge):
    def __init__(self, engine):
        super().__init__(engine)

    def upgrade(self):
        self.engine.curr_mileage = "600 miles/charge"


if __name__ == "__main__":
    e = Electric()
    t = Tesla(e)
    t.stats()
    t.upgrade()
    t.stats()
