import os, json
import collections


# Proxy pattern is used for forwrading the calls to the original library or real service
# proxy pattern helps in intercepting and making changes.
# this is also helpful in interchangeably used between already used clients calling the original library

class DOT:

    def list_vehicles(self):
        print("call DOT and list a set of vehicles")

    def list_impounded(self):
        print("call DOT and list a set of impounded vehicles")

    def impound_vehicle(self, vehicle_no):
        print(f"{vehicle_no} is impounded")


class DOTProxy:

    def __init__(self):
        self.dot = DOT()

    def list_vehicles(self):
        self.dot.list_vehicles()

    def list_impounded(self):
        self.dot.list_impounded()
        print("to be destroyed if not claimed")

    def impound_vehicle(self, vehicle_no):
        if self.verify(vehicle_no):
            print(f"Checking {vehicle_no}")

        self.dot.impound_vehicle(vehicle_no)


def main():
    pass


if __name__ == "__main__":
    main()
