import unittest
from main import *

class DummyTests (unittest.TestCase):

    def test_obvious (self):
        self.assertEqual(1, 1)

    def test_creating_a_basic_app_object (self):
        converter = TextToDate()
        self.assertIsInstance(converter, TextToDate)

class convertNumericInputs (unittest.TestCase):
    def test_passing_a_numerical_date_return_same(self):
        converter = TextToDate()
        date = converter.convert("02/03/1384")
        self.assertEqual(date, "02/03/1384")

    def test_passing_none_standard_numerical_returns_standard_numerical(self):
        converter = TextToDate()
        self.assertEqual(converter.convert("2/3/1345"), "02/03/1345")
        self.assertEqual(converter.convert("2/3/45"), "02/03/0045")

if __name__ == '__main__':
    unittest.main()
