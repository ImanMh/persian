import unittest
from main import *

class DummyTests (unittest.TestCase):

    def test_obvious(self):
        self.assertEqual(1, 1)

    def test_creating_a_basic_app_object(self):
        converter = TextToNumber()
        self.assertIsInstance(converter, TextToNumber)

class converter_single_digit_numbers (unittest.TestCase):

    def test_can_convert_one(self):
        self.assertEqual(TextToNumber.convert('yek'), 1);

    def test_can_convert_zero(self):
        self.assertEqual(TextToNumber.convert('sefr'), 0);


class convert_irregulars (unittest.TestCase):

    def test_can_conver_ninteen(self):
        self.assertEqual(TextToNumber.convert('noonzdah'), 19);

    def test_can_conver_ten(self):
        self.assertEqual(TextToNumber.convert('dah'), 10);


class convert_two_digits (unittest.TestCase):

    def test_can_conver_twenty(self):
        self.assertEqual(TextToNumber.convert('bist'), 20);

    def test_can_convert_two_part_two_digit_number(self):
        self.assertEqual(TextToNumber.convert('bist o yek'), 21)

    def test_can_convert_one_part_two_digit_numbers(self):
        self.assertEqual(TextToNumber.convert('si'), 30)

    def test_can_convert_ninty_nine(self):
        self.assertEqual(TextToNumber.convert('navad o noh'), 99)


class convert_three_digits (unittest.TestCase):

    def test_can_convert_one_part_three_digit(self):
        self.assertEqual(TextToNumber.convert('sad'), 100)

    def test_can_convert_two_part_three_digit(self):
        self.assertEqual(TextToNumber.convert('sad o chehel'), 140)

    def test_convert_three_part_three_digit(self):
        self.assertEqual(TextToNumber.convert('sad o chehel o chahar'), 144)

    def test_convert_three_digit_with_middle_part_missing(self):
        self.assertEqual(TextToNumber.convert('sad o chahar'), 104)








if __name__ == '__main__':
    unittest.main()
