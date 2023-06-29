import unittest
from spot_impl import SpotImpl

class TestSpotImpl(unittest.TestCase):

    def setUp(self):
        self.valid_construct = SpotImpl("a", 1)
        self.valid_construct2 = SpotImpl("h", 8)
        self.valid_construct3 = SpotImpl("e", 4)

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

    def test_distanceTo(self):
        self.assertEqual(self.valid_construct.distanceTo(SpotImpl("a", 1)), 0)
        self.assertEqual(self.valid_construct.distanceTo(SpotImpl("a", 2)), 1)
        self.assertEqual(self.valid_construct.distanceTo(SpotImpl("a", 8)), 7)
        self.assertEqual(self.valid_construct.distanceTo(SpotImpl("b", 7)), 6.082762530298219)

    def test_distanceToNorm(self):
        self.assertEqual(self.valid_construct.distanceToNorm(SpotImpl("a", 2)), 1)
        self.assertEqual(self.valid_construct.distanceToNorm(SpotImpl("h", 8)), 0)
        self.assertEqual(self.valid_construct3.distanceToNorm(SpotImpl("e", 3)), 1)
        self.assertEqual(self.valid_construct3.distanceToNorm(SpotImpl("f", 4)), 1)
        self.assertEqual(self.valid_construct2.distanceToNorm(SpotImpl("a", 1)), 0)

    if __name__ == '__main__':
        unittest.main()