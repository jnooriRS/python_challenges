import unittest
from min_tickets import mincostTickets


class TestCoinResult(unittest.TestCase):
    def test_change(self):
        self.assertEqual(mincostTickets(5, [1, 2, 5]), 4)

    def test_input_type(self):
        self.assertRaises(ValueError, mincostTickets("x", ["x, y, z"]), "some-string")


# python -m unittest test_filename.py
if __name__ == "__main__":
    unittest.main()

# Input days = [1, 4, 6, 7, 8, 20] costs = [2,7,15]
# output 11
# day 1 you buy cost[0] = 2
# day 3 you buy cost[1] = 7
# day 20 you buy cost[0] = 2
