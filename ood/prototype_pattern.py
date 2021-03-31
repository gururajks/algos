import os, json
import collections
import random
import abc
import copy


class VehicleRegistry:
    def __init__(self):
        pass


class Vehicle:
    def __init__(self):
        pass

    def run(self):
        pass

    def print(self):
        pass


class Wheel:
    def __init__(self):
        self.radius = 10
        self.pressure = 32


class Engine:
    def __init__(self, hp):
        self.hp = hp


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.name = "Car"
        self.wheels = [Wheel()] * 4
        self.random_stuff = [random.randint(1, 20) for _ in range(20)]
        self.engine = Engine(180)

    def print(self):
        print(f"Name: {self.name}    {self.wheels}     {self.random_stuff}")

    def __copy__(self):
        name = self.name
        wheels = self.wheels
        random_stuff = self.random_stuff
        engine = self.engine
        new = self.__class__(
            name, random_stuff, engine, wheels
        )
        return new

    def __deepcopy__(self, memodict={}):
        name = copy.deepcopy(self.name)
        wheels = copy.deepcopy(self.wheels)
        random_stuff = copy.deepcopy(self.random_stuff)
        engine = copy.deepcopy(self.engine)
        new = self.__class__(
            name, random_stuff, engine, wheels
        )
        return new


class Ship(Vehicle):
    def __init__(self):
        super().__init__()
        self.name = "Ship"
        self.wheels = None
        self.random_stuff = [random.randint(1, 20) for _ in range(20)]
        self.engine = Engine(1800)

    def print(self):
        print(f"Name: {self.name}    {self.wheels}     {self.random_stuff}")

    def __copy__(self):
        name = self.name
        wheels = self.wheels
        random_stuff = self.random_stuff
        engine = self.engine
        new = self.__class__(
            name, random_stuff, engine, wheels
        )
        return new

    def __deepcopy__(self, memodict={}):
        name = copy.deepcopy(self.name)
        wheels = copy.deepcopy(self.wheels)
        random_stuff = copy.deepcopy(self.random_stuff)
        engine = copy.deepcopy(self.engine)
        new = self.__class__(
            name, random_stuff, engine, wheels
        )
        return new


if __name__ == "__main__":
    c = Car()
    print(c)
    c1 = copy.deepcopy(c)
    print(c1)
