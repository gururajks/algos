import os, json
import collections
import unittest


def is_string_unique(input_str):
    hash_table = {}
    for s in input_str:
        if s in hash_table:
            hash_table[s] += 1
        else:
            hash_table[s] = 1

    for k, v in hash_table.items():
        if v > 1:
            return False
    return True


class MyTestCase(unittest.TestCase):
    def test_something(self):
        inputstr = "abdc"
        self.assertEqual(is_string_unique(inputstr), True)


if __name__ == '__main__':
    unittest.main()
c