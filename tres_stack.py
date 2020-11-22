import os, json
import collections


class Tres_Stack:
    def __init__(self):
        self.l = []
        self.l.append(None)

        # stack number to last index
        self.stack_map = {
            1: -2,
            2: -1,
            3: 0
        }

    def pop(self, stack_number):
        idx = self.stack_map[stack_number]
        val = self.l[idx]
        self.l[idx] = None
        if self.stack_map[stack_number] > 3:
            self.stack_map[stack_number] -= 3

        # # clean up later to reduce the length of the list
        # while len(self.l) > max(self.stack_map.values()) + 1:
        #     self.l.pop()

        return val

    def push(self, item, stack_number):
        expected_idx = self.stack_map[stack_number] + 3
        while expected_idx >= len(self.l):
            self.l.append(None)

        self.l[expected_idx] = item
        self.stack_map[stack_number] = expected_idx


if __name__ == "__main__":
    main()
