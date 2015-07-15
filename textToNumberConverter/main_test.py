import unittest
from main import *


class DummyTests (unittest.TestCase):

    def test_obvious(self):
        self.assertEqual(1, 1)

    def test_creating_a_basic_app_object(self):
        converter = TextToNumber()
        self.assertIsInstance(converter, TextToNumber)


class ConverterSingleDigitNumbers (unittest.TestCase):

    def test_convert_one(self):
        self.assertEqual(TextToNumber.convert('yek'), 1);

    def test_convert_zero(self):
        self.assertEqual(TextToNumber.convert('sefr'), 0);


class ConvertIrregulars (unittest.TestCase):

    def test_convert_nineteen(self):
        self.assertEqual(TextToNumber.convert('noonzdah'), 19);

    def test_convert_ten(self):
        self.assertEqual(TextToNumber.convert('dah'), 10);


class ConvertTwoDigits (unittest.TestCase):

    def test_convert_twenty(self):
        self.assertEqual(TextToNumber.convert('bist'), 20);

    def test_convert_two_part_two_digit_number(self):
        self.assertEqual(TextToNumber.convert('bist o yek'), 21)

    def test_convert_one_part_two_digit_numbers(self):
        self.assertEqual(TextToNumber.convert('si'), 30)

    def test_convert_ninety_nine(self):
        self.assertEqual(TextToNumber.convert('navad o noh'), 99)


class ConvertThreeDigits (unittest.TestCase):

    def test_convert_one_part_three_digit(self):
        self.assertEqual(TextToNumber.convert('sad'), 100)

    def test_convert_two_part_three_digit(self):
        self.assertEqual(TextToNumber.convert('sad o chehel'), 140)

    def test_convert_three_part_three_digit(self):
        self.assertEqual(TextToNumber.convert('sad o chehel o chahar'), 144)

    def test_convert_three_digit_with_middle_part_missing(self):
        self.assertEqual(TextToNumber.convert('sad o chahar'), 104)

    def test_convert_three_digit_with_irregular_ending(self):
        self.assertEqual(TextToNumber.convert('sad o dah'), 110)


class ConvertFourDigits (unittest.TestCase):

    def test_convert_one_part_four_digits(self):
        self.assertEqual(TextToNumber.convert('hezar'), 1000)

    def test_convert_two_part_four_digits(self):
        self.assertEqual(TextToNumber.convert('hezar o sad'), 1100)

    def test_convert_three_part_four_digits(self):
        self.assertEqual(TextToNumber.convert('hezar o sad o dah'), 1110)

    def test_convert_four_part_four_digits(self):
        self.assertEqual(TextToNumber.convert('hezar o sad o yazdah'), 1111)

    def test_convert_two_part_four_digits_two_middle_digits_zero(self):
        self.assertEqual(TextToNumber.convert('hezar o yek'), 1001)

    def test_convert_one_part_with_multiplier(self):
        self.assertEqual(TextToNumber.convert('do hezar'), 2000)


if __name__ == '__main__':
    unittest.main()
