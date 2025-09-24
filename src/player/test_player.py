"""Test class for the player class"""
import unittest
from player import Player


class TestPlayerClass(unittest.TestCase):

    def setUp(self):
        """Create a player instance used in the tests below"""
        self.testPlayer = Player("Bob")

    def test_getScore(self):
        """Returns the score of the player instance"""
        self.assertEqual(self.testPlayer.get_score(), 0) # The score should be 0 to begin with
        self.assertNotEqual(self.testPlayer.get_score(), 10) # The score should not be anything other than 0

    def test_addScore(self):
        """Adds a score to the player instance"""
        self.testPlayer.add_score(5) # Add 5 to the score
        self.assertEqual(self.testPlayer.get_score(), 5) # Score should now be 5
        self.testPlayer.add_score(7) # Add 7 to the score
        self.assertEqual(self.testPlayer.get_score(), 12) # Score should now be 12
        self.testPlayer.add_score(3) # Add 3 to the score
        self.assertNotEqual(self.testPlayer.get_score(), 16) # Score should now be 15

    def test_getName(self):
        """Returns the name of the player instance"""
        self.assertEqual(self.testPlayer.get_name(), "Bob") # The object was instansiated with the name Bob
        self.assertNotEqual(self.testPlayer.get_name(), "Not Bob") # The name attribute should not be anything other than Bob

    def test_changeName(self):
        """Changes the name of the player instance"""
        new_name = "Alice"
        self.testPlayer.change_name(new_name) # Change name to Alice
        self.assertEqual(self.testPlayer.get_name(), new_name) # The new name should be Alice

        new_name = "Frank"
        self.testPlayer.change_name(new_name) # Change name to Frank
        self.assertEqual(self.testPlayer.get_name(), new_name) # The new name should be Frank

        new_name = "Bill"
        self.testPlayer.change_name(new_name) # Change name to Bill
        self.assertEqual(self.testPlayer.get_name(), new_name) # The new name should be Bill

if __name__ == "__main__":
    unittest.main()
