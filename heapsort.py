import os, json
import collections


class Iterator:

    def __init__(self, val_list):
        self.iter_ptr = 0
        self.val_list = val_list

    def hasNext(self):
        return self.iter_ptr < len(self.val_list)

    def next(self):
        if self.hasNext():
            next_val = self.val_list[self.iter_ptr]
            self.iter_ptr += 1
            return next_val


if __name__ == "__main__":
    main()
