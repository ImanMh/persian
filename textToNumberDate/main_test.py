import unittest
from main import *

class DummyTest (unittest.TestCase):

    def test_obvious (self):
        self.assertEqual(1, 1)

    def test_creating_a_basic_app_object (self):
        converter = TextToNumberDate()
        self.assertIsInstance(converter, TextToNumberDate)


if __name__ == '__main__':
    unittest.main()
