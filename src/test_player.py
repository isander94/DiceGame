"""Test class for the player class."""

import unittest
from player import Player


class TestPlayerClass(unittest.TestCase):
    """Test the player class."""

    def setUp(self):
        """Create a player instance used in the tests below."""
        self.test_player = Player("Bob", 1, 6)

    def test_instance(self):
        """Test what class the object is instansiated from."""
        # test_player should be of class Player
        self.assertIsInstance(self.test_player, Player)

    def test_attributes(self):
        """Check that the Player class have their attributes assigned."""
        # The name should not be empty when the instance is created
        self.assertIsNotNone(self.test_player.name)
        # The score should not be empty when the instance is created
        self.assertIsNotNone(self.test_player.score)
        # The associated dice object should be initialized
        self.assertIsNotNone(self.test_player.dice)

    def test_get_score(self):
        """Returns the score of the player instance."""
        # The score should be of class int
        self.assertIsInstance(self.test_player.get_score(), int)
        # The score should be 0 to begin with
        self.assertEqual(self.test_player.get_score(), 0)
        # The score should not be anything other than 0
        self.assertNotEqual(self.test_player.get_score(), 10)

    def test_add_score(self):
        """Adds a score to the player instance."""
        # Add 5 to the score
        self.test_player.add_score(5)
        # Score should now be 5
        self.assertEqual(self.test_player.get_score(), 5)
        # Add 7 to the score
        self.test_player.add_score(7)
        # Score should now be 12
        self.assertEqual(self.test_player.get_score(), 12)
        # Add 3 to the score
        self.test_player.add_score(3)
        # Score should now be 15 and not 16
        self.assertNotEqual(self.test_player.get_score(), 16)
        # Add 0 to the score - it should remain the same
        self.test_player.add_score(0)
        # Score should still be 15
        self.assertEqual(self.test_player.get_score(), 15)

    def test_add_score_negative(self):
        """Adds a negative score and checks the total score."""
        # Add 5 to the score
        self.test_player.add_score(5)
        # Add -2. This should not subtract from the total score
        self.test_player.add_score(-2)
        # The score should still be 5
        self.assertEqual(self.test_player.get_score(), 5)

    def test_add_score_multiple(self):
        """Adds a score three times and checks for the correct sum."""
        # Add 2 to the score
        self.test_player.add_score(2)
        # Add 8 to the score
        self.test_player.add_score(8)
        # Add 4 to the score
        self.test_player.add_score(4)
        # The total score should now be 14
        self.assertEqual(self.test_player.get_score(), 14)

    def test_get_name(self):
        """Returns the name of the player instance."""
        # The name attribute should be of class string
        self.assertIsInstance(self.test_player.get_name(), str)
        # The object was instansiated with the name Bob
        self.assertEqual(self.test_player.get_name(), "Bob")
        # The name attribute should not be anything other than Bob
        self.assertNotEqual(self.test_player.get_name(), "Not Bob")

    def test_change_name(self):
        """Changes the name of the player instance multiple times."""
        new_name = "Alice"
        # Change name to Alice
        self.test_player.change_name(new_name)
        # The new name should be Alice
        self.assertEqual(self.test_player.get_name(), new_name)
        
        new_name = "Frank"
        # Change name to Frank
        self.test_player.change_name(new_name)
        # The new name should be Frank  
        self.assertEqual(self.test_player.get_name(), new_name)

        new_name = "Bill"
        # Change name to Bill
        self.test_player.change_name(new_name)
        # The new name should be Bill
        self.assertEqual(self.test_player.get_name(), new_name)

    def test_change_name_empty(self):
        """Try to change the name to an empty string."""
        # Should return false as we're trying to set an empty name
        self.assertFalse(self.test_player.change_name(""))
        # Check that the name is still Bob and not an empty name
        self.assertEqual(self.test_player.get_name(), "Bob")

    def test_roll_dice(self):
        """Test rolling the die and check what it returns."""
        # Roll the die
        roll = self.test_player.roll_dice()
        # Create a boolean variable checking the range
        is_within_range = 1 <= roll <= 6
        # dice attribute was instansiated with values 1 and 6 - It should pass
        self.assertTrue(is_within_range)


if __name__ == "__main__":
    unittest.main()
