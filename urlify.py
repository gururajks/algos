import unittest


def urlify(inputstr):
    return inputstr


class MyUnitTest(unittest.TestCase):
    def test_urlify(self):
        name = "Mr John Smith      "
        result = urlify(name)
        self.assertEqual(result, "Mr%20John%20Smith")

    def test_urlify_fail(self):
        name = "Mr John Smith      "
        result = urlify(name)
        self.assertNotEqual(result, "Mr%20John%20Smith")


if __name__ == '__main__':
    unittest.main()
