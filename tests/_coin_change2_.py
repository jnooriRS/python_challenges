import unittest

from coin_change2 import change


class TestCoinResult(unittest.TestCase):
    def test_number(self):
        self.assertEqual(fib_find(5), 5)
        self.assertEqual(fib_find(6), 8)
        self.assertEqual(fib_find(7), 13)

    def test_input_type(self):
        self.assertRaises(ValueError, fib_find, "some-string")


if __name__ == "__main__":
    unittest.main()
