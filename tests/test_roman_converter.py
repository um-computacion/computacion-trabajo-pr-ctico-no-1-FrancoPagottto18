import unittest
from src.roman_converter import roman_to_decimal

class TestRomanConverter(unittest.TestCase):
    def test_basic_numbers(self):
        self.assertEqual(roman_to_decimal(1), "I")
        self.assertEqual(roman_to_decimal(5), "V")
        self.assertEqual(roman_to_decimal(10), "X")

    def test_subtraction_rules(self):
        self.assertEqual(roman_to_decimal(4), "IV")
        self.assertEqual(roman_to_decimal(9), "IX")
        self.assertEqual(roman_to_decimal(40), "XL")
        self.assertEqual(roman_to_decimal(90), "XC")

    def test_complex_numbers(self):
        self.assertEqual(roman_to_decimal(49), "XLIX")
        self.assertEqual(roman_to_decimal(99), "XCIX")
        self.assertEqual(roman_to_decimal(499), "CDXCIX")
        self.assertEqual(roman_to_decimal(999), "CMXCIX")
        self.assertEqual(roman_to_decimal(3999), "MMMCMXCIX")

if __name__ == '__main__':
    unittest.main()