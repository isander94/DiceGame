"""Unit testing for dice class."""
import unittest

from dice import Dice


class TestDiceClass(unittest.TestCase):
    """Setting up with dice class, and testing it."""

    def setUp(self):
        """Create different dice."""
        self.my_dice1 = Dice(1, 6)
        self.my_dice2 = Dice(1, 12)
        self.my_dice3 = Dice(6, 18)

    def test_roll_dice(self):
        """Checks if die lands on number between high and low on roll."""
        roll_1 = self.my_dice1.roll_dice()
        expected1 = roll_1 >= 1 and roll_1 <= 6
        self.assertTrue(expected1)

        roll_2 = self.my_dice2.roll_dice()
        expected2 = roll_2 >= 1 and roll_2 <= 12
        self.assertTrue(expected2)

        roll_3 = self.my_dice3.roll_dice()
        expected3 = roll_3 >= 6 and roll_3 <= 18
        self.assertTrue(expected3)

    def test_low_number(self):
        """Checks that the lowest number on the die is the lowest."""
        expected_low1 = 1
        self.assertEqual(expected_low1, self.my_dice1.low)

        expected_low2 = 1
        self.assertEqual(expected_low2, self.my_dice2.low)

        expected_low3 = 6
        self.assertEqual(expected_low3, self.my_dice3.low)

    def test_high_number(self):
        """Checks that the highest number on the die is the highest."""
        expected_high1 = 6
        self.assertEqual(expected_high1, self.my_dice1.high)

        expected_high2 = 12
        self.assertEqual(expected_high2, self.my_dice2.high)

        expected_high3 = 18
        self.assertEqual(expected_high3, self.my_dice3.high)


if __name__ == "__main__":
    unittest.main()
