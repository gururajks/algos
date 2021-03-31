import os, json
import collections
import abc

# a decorator is used to extend the behavior during runtime with a wrapper

class Engine:
    def __init__(self):
        print("Create Engine")

    @abc.abstractmethod
    def start_fuel_flow(self):
        pass

    @abc.abstractmethod
    def power(self):
        pass


class UpgradedEngine(Engine):
    def __init__(self):
        print('upgrade the engine')

    def start_fuel_flow(self):
        print('start the fule flow')

    def power(self):
        print('get power from side engines')


class SportsEngine(Engine):

    def __init__(self, improved_engine):
        self.improved_engine = improved_engine

    def start_fuel_flow(self):
        self.improved_engine.start_fuel_flow()

    def power(self):
        self.improved_engine.power()


class HybridEngine(Engine):

    def __init__(self, improved_engine):
        self.improved_engine = improved_engine

    def start_fuel_flow(self):
        self.improved_engine.start_fuel_flow()

    def power(self):
        self.improved_engine.power()


def main():

    engine_2020 = UpgradedEngine()
    sp = SportsEngine(engine_2020)
    sp.power()
    sp.start_fuel_flow()

    h = HybridEngine(engine_2020)
    h.power()
    h.start_fuel_flow()




if __name__ == "__main__":
    main()
