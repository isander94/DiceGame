"""Test class for the player class"""
import unittest
from player import Player


class TestPlayerClass(unittest.TestCase):
    """Test the player class"""

    def setUp(self):
        """Create a player instance used in the tests below"""
        self.testPlayer = Player("Bob", 1, 6)

    def test_instance(self):
        """Test what class the object is instansiated from"""
        self.assertIsInstance(self.testPlayer, Player) # testPlayer should be of class Player

    def test_attributes(self):
        """Test to check that the instance of the Player class have their attributes assigned"""
        self.assertIsNotNone(self.testPlayer.name) # The name should not be empty when the instance is created
        self.assertIsNotNone(self.testPlayer.score) # The score should not be empty when the instance is created
        self.assertIsNotNone(self.testPlayer.dice) # The associated dice object should be initialized

    def test_getScore(self):
        """Returns the score of the player instance"""
        self.assertIsInstance(self.testPlayer.get_score(), int) # The score should be of class int
        self.assertEqual(self.testPlayer.get_score(), 0) # The score should be 0 to begin with
        self.assertNotEqual(self.testPlayer.get_score(), 10) # The score should not be anything other than 0

    def test_addScore(self):
        """Adds a score to the player instance"""
        self.testPlayer.add_score(5) # Add 5 to the score
        self.assertEqual(self.testPlayer.get_score(), 5) # Score should now be 5
        self.testPlayer.add_score(7) # Add 7 to the score
        self.assertEqual(self.testPlayer.get_score(), 12) # Score should now be 12
        self.testPlayer.add_score(3) # Add 3 to the score
        self.assertNotEqual(self.testPlayer.get_score(), 16) # Score should now be 15 and not 16
        self.testPlayer.add_score(0) # Add 0 to the score - it should remain the same
        self.assertEqual(self.testPlayer.get_score(), 15) # Score should still be 15

    def test_addScore_negative(self):
        """Adds a negative score and checks the total score"""
        self.testPlayer.add_score(5) # Add 5 to the score
        self.testPlayer.add_score(-2) # Add -2. This should not subtract from the total score
        self.assertEqual(self.testPlayer.get_score(), 5) # The score should still be 5

    def test_addScore_multiple(self):
        """Adds a score three times and checks for the correct sum"""
        self.testPlayer.add_score(2) # Add 2 to the score
        self.testPlayer.add_score(8) # Add 8 to the score
        self.testPlayer.add_score(4) # Add 4 to the score
        self.assertEqual(self.testPlayer.get_score(), 14) # The total score should now be 14

    def test_getName(self):
        """Returns the name of the player instance"""
        self.assertIsInstance(self.testPlayer.get_name(), str) # The name attribute should be of class string
        self.assertEqual(self.testPlayer.get_name(), "Bob") # The object was instansiated with the name Bob
        self.assertNotEqual(self.testPlayer.get_name(), "Not Bob") # The name attribute should not be anything other than Bob

    def test_changeName(self):
        """Changes the name of the player instance multiple times"""
        new_name = "Alice"
        self.testPlayer.change_name(new_name) # Change name to Alice
        self.assertEqual(self.testPlayer.get_name(), new_name) # The new name should be Alice

        new_name = "Frank"
        self.testPlayer.change_name(new_name) # Change name to Frank
        self.assertEqual(self.testPlayer.get_name(), new_name) # The new name should be Frank

        new_name = "Bill"
        self.testPlayer.change_name(new_name) # Change name to Bill
        self.assertEqual(self.testPlayer.get_name(), new_name) # The new name should be Bill

    def test_changeName_empty(self):
        """Try to change the name to an empty string"""
        self.assertFalse(self.testPlayer.change_name("")) # Should return false as we're trying to set an empty name
        self.assertEqual(self.testPlayer.get_name(), "Bob") # Check that the name is still Bob and not an empty name

    def test_rollDice(self):
        """Test rolling the die and check what it returns"""
        roll = self.testPlayer.roll_dice() # Roll the die
        is_within_range = roll >= 1 and roll <= 6 # Create a boolean variable checking the range
        self.assertTrue(is_within_range) # The dice attribute was instansiated with parameters 1 and 6 - It should pass


if __name__ == "__main__":
    unittest.main()
