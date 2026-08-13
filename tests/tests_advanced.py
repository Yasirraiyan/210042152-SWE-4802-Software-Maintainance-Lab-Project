import unittest

from calculator.advanced import (
    square_root,
    cube_root,
    power,
    factorial,
    percentage
)


class TestAdvancedCalculator(unittest.TestCase):

    def test_square_root(self):
        self.assertEqual(square_root(25), 5)

    def test_cube_root(self):
        self.assertAlmostEqual(cube_root(125), 5)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_negative_square_root(self):
        with self.assertRaises(ValueError):
            square_root(-25)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

    def test_percentage(self):
        self.assertEqual(percentage(200, 10), 20)


if __name__ == "__main__":
    unittest.main()
