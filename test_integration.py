import unittest

from calculator.basic import add
from calculator.advanced import power
from calculator.validator import validate_number


class TestIntegration(unittest.TestCase):

    def test_calculation_flow(self):
        a = validate_number("10")
        b = validate_number("5")

        basic_result = add(a, b)
        final_result = power(basic_result, 2)

        self.assertEqual(final_result, 225)


if __name__ == "__main__":
    unittest.main()