# unit_tests.py
#
# Created: Apr/9/2023
#
# Test functionality of program using the unit test framework

import unittest
from move_impl import MoveImpl
from spot_impl import SpotImpl

class TestMoveImpl(unittest.TestCase):
    # Test MoveImpl constructs properly
    def setUp(self):
        self.move = MoveImpl(SpotImpl("a", 2), SpotImpl("h", 4))

    def test_getLocation(self):
        self.assertEqual(self.move.getLocation(), self.move.location)
        self.assertEqual(self.move.getLocation().row, "2")
        self.assertEqual(self.move.getLocation().col, "a")

    def test_getDestination(self):
        self.assertEqual(self.move.getDestination(), self.move.destination)
        self.assertEqual(self.move.getDestination().row, "4")
        self.assertEqual(self.move.getDestination().col, "h")

    def test_invalid(self):
        threw_error = False
        try:
            invalid_move = MoveImpl(SpotImpl("i", 1), SpotImpl("h", 4))
        except ValueError:
            threw_error = True

        self.assertTrue(threw_error)

if __name__ == '__main__':
    unittest.main()
