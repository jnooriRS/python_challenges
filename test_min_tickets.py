import unittest
from min_tickets import solution


class TestCoinResult(unittest.TestCase):
    def test_change(self):
        self.assertEqual(
            solution.mincostTickets(self, [1, 4, 5, 6, 7, 8, 20], [2, 7, 15]),
            10
            # purposfully created error to see what the coreect return value should be in terminal
        )

    def test_input_type(self):
        with self.assertRaises(TypeError):
            solution.mincostTickets(self, ["x"], ["x, y, z"])


# python -m unittest test_min_tickets.py
if __name__ == "__main__":
    unittest.main()

# Input days = [1, 4, 6, 7, 8, 20] costs = [2,7,15]
# output 11
# day 1 you buy cost[0] = 2
# day 3 you buy cost[1] = 7
# day 20 you buy cost[0] = 2


def test_split(self):
    s = "hello world"
    self.assertEqual(s.split(), ["hello", "world"])
    # check that s.split fails when the separator is not a string
    with self.assertRaises(TypeError):
        s.split(2)
