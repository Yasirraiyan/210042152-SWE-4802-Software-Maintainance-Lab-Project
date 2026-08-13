import unittest

from calculator.validator import validate_number


class TestValidator(unittest.TestCase):

    def test_valid_number(self):
        self.assertEqual(validate_number("25"), 25.0)

    def test_decimal_number(self):
        self.assertEqual(validate_number("25.5"), 25.5)

    def test_invalid_number(self):
        with self.assertRaises(ValueError):
            validate_number("abc")

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            validate_number("")


if __name__ == "__main__":
    unittest.main()