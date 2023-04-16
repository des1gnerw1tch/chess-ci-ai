import unittest
from spot_impl import SpotImpl

class TestSpotImpl(unittest.TestCase):

    def setUp(self):
        self.valid_construct = SpotImpl("a", 1)
        self.valid_construct2 = SpotImpl("h", 8)

    def test_valid(self):
        self.assertEqual(self.valid_construct.col, "a")
        self.assertEqual(self.valid_construct.row, "1")
        self.assertEqual(self.valid_construct2.col, "h")
        self.assertEqual(self.valid_construct2.row, "8")

    def test_invalid(self):
        threw_error = False
        try:
            invalid_spot = SpotImpl("i", 1)
        except ValueError:
            threw_error = True

        self.assertTrue(threw_error)
    
    def test_invalid2(self):
        threw_error = False
        try:
            invalid_spot = SpotImpl("c", 9)
        except ValueError:
            threw_error = True

        self.assertTrue(threw_error)
    
    if __name__ == '__main__':
        unittest.main()