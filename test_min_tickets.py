import unittest
from min_tickets import change


class TestCoinResult(unittest.TestCase):
    def test_change(self):
        self.assertEqual(change(5, [1, 2, 5]), 4)

    def test_input_type(self):
        self.assertRaises(ValueError, change("x", ["x, y, z"]), "some-string")


# python -m unittest test_filename.py
if __name__ == "__main__":
    unittest.main()
