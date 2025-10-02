"""Test class for the Game class"""

import unittest
from game import Game

class TestGameClass(unittest.TestCase):
    """Test the Game class"""
    
    def setUp(self):
        """Create a Game instance"""
        game = Game()
        
    def test_instance(self):
        """Test what class the object is instansiated from"""
        self.assertIsInstance(self.testPlayer, Game) # game should be of class Game
        
    