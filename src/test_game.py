"""Test class for the Game class"""

import unittest
from game import Game
from player import Player

class TestGameClass(unittest.TestCase):
    """Test the Game class"""
    
    def setUp(self):
        """Create a Game instance"""
        self.game = Game()
        self.player = Player("Testplayer", 1, 6)
        
    def test_instance(self):
        """Test what class the object is instansiated from"""
        self.assertIsInstance(self.game, Game) # game should be of class Game
        
    def test_cheat(self):
        """Test the cheat command, adding 100 points. The new player score should be 100"""
        self.game.cheat(self.player)
        self.assertEqual(self.player.get_score(), 100) # The score should be equal to 100
        self.assertNotEqual(self.player.get_score(), 50) # The score should only be equal to 100
        
    def test_checkIfNotWon(self):
        """Add a score below 100 and check if the player has won. Should return False"""
        self.player.add_score(15)
        has_won = self.game.check_if_won(self.player)
        self.assertFalse(has_won) # Should return False as the score is below 100
        self.player.add_score(37)
        has_won = self.game.check_if_won(self.player)
        self.assertFalse(has_won) # Should still return False as the score is still below 100
        
    def test_checkIfWon(self):
        """Add 100 points to the player and check if the player has one. Should return True"""
        self.player.add_score(100)
        has_won = self.game.check_if_won(self.player)
        self.assertTrue(has_won) # Should return True as the score is now atleast 100 points
        self.player.add_score(25) # Add another 25 points
        has_won = self.game.check_if_won(self.player)
        self.assertTrue(has_won) # Should still return True as the score is still atleast 100 points
        
        
    
        
if __name__ == "__main__":
    unittest.main()
    