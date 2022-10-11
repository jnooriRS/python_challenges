import unittest


class TestCoinResult(unittest.TestCase):
    def test_change(self):
        self.assertEqual(change(5), 4)

    def test_input_type(self):
        self.assertRaises(ValueError, change, "some-string")


if __name__ == "__main__":
    unittest.main()
