import unittest
from collections import Counter


def check_permutation(input1, input2):
    c1 = Counter(input1)
    c2 = Counter(input2)

    for k, v in c1.items():
        if c2[k] != v:
            return False

    return True


class check_permutation_unit_test(unittest.TestCase):
    def test_check_permutation(self):
        input1 = "abba"
        input2 = "bbaa"
        self.assertEqual(check_permutation(input1, input2), True)

    def test_check_permutation_fail(self):
        input1 = "abbc"
        input2 = "bbcaa"
        self.assertEqual(check_permutation(input1, input2), False)


if __name__ == '__main__':
    unittest.main()
