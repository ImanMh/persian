import unittest
from main import *

class DummyTests (unittest.TestCase):

    def test_obvious (self):
        self.assertEqual(1, 1)

    def test_creating_a_basic_app_object (self):
        converter = TextToNumber()
        self.assertIsInstance(converter, TextToNumber)

class convertNumericInputs (unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
