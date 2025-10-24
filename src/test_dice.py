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

    def test_instance(self):
        """Test what class the object is instansiated from."""
        self.assertIsInstance(self.my_dice1, Dice)
        self.assertIsInstance(self.my_dice2, Dice)
        self.assertIsInstance(self.my_dice3, Dice)

    def test_attributes(self):
        """Check that instance of class Dice have attributes assigned."""
        self.assertIsNotNone(self.my_dice1.low)
        self.assertIsNotNone(self.my_dice1.high)

        self.assertIsNotNone(self.my_dice2.low)
        self.assertIsNotNone(self.my_dice2.high)

        self.assertIsNotNone(self.my_dice3.low)
        self.assertIsNotNone(self.my_dice3.high)

    def test_roll(self):
        """Checks if die lands on number between high and low on roll."""
        roll_1 = self.my_dice1.roll()
        expected1 = 1 <= roll_1 <= 6
        self.assertTrue(expected1)

        roll_2 = self.my_dice2.roll()
        expected2 = 1 <= roll_2 <= 12
        self.assertTrue(expected2)

        roll_3 = self.my_dice3.roll()
        expected3 = 6 <= roll_3 <= 18
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

    def test_same_low_and_high_returns_constant(self):
        """If low == high, roll() should always return that number."""
        dice = Dice(5, 5)
        for i in range(10):
            self.assertEqual(dice.roll(), 5)

    def test_attribute_types(self):
        """Ensure attributes are integers."""
        self.assertIsInstance(self.my_dice1.low, int)
        self.assertIsInstance(self.my_dice1.high, int)

    def test_invalid_range_raises_error(self):
        """Test that invalid range raises ValueError."""
        with self.assertRaises(ValueError):
            Dice(10, 1)

    def test_non_integer_values_raise_error(self):
        """Test that Dice does not accept float or string values."""
        with self.assertRaises(TypeError):
            Dice(1.5, 6)
        with self.assertRaises(TypeError):
            Dice(1, 6.2)
        with self.assertRaises(TypeError):
            Dice("1", 6)
        with self.assertRaises(TypeError):
            Dice(1, "6")

    def test_multiple_rolls_are_independent(self):
        """Ensure multiple rolls return values within bounds each time."""
        for i in range(100):
            roll = self.my_dice1.roll()
            self.assertTrue(1 <= roll <= 6)


if __name__ == "__main__":
    unittest.main()
