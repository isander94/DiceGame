"""Test class for the Game class"""

import unittest
from unittest.mock import patch
from game import Game
from player import Player

class TestGameClass(unittest.TestCase):
    """Test the Game class"""
    
    def setUp(self):
        """Create a Game instance"""
        self.game = Game()
        self.player1 = Player("Testplayer#1", 1, 6)
        self.player2 = Player("Testplayer#2", 1, 6)
        self.players = [self.player1, self.player2]
        
    def test_attributes_init(self):
        """Test that the initial attributes of the Game object are initialized and not none"""
        self.assertIsNotNone(self.game.game_is_active) 
        self.assertIsNotNone(self.game.round_score)
        
    def test_attributes_value(self):
        """Test that the initial attributes of the Game object have the correct values"""
        self.assertEqual(self.game.game_is_active, True)
        self.assertNotEqual(self.game.game_is_active, False)
        self.assertEqual(self.game.round_score, 0)
        self.assertNotEqual(self.game.round_score, 50)
        
    def test_instance(self):
        """Test what class the object is instansiated from"""
        self.assertIsInstance(self.game, Game) # game should be of class Game
        
    def test_cheat(self):
        """Test the cheat command, adding 100 points. The new player score should be 100"""
        self.game.cheat(self.player1)
        self.assertEqual(self.player1.get_score(), 100) # The score should be equal to 100
        self.assertNotEqual(self.player1.get_score(), 50) # The score should only be equal to 100
        
    def test_checkIfNotWon(self):
        """Add a score below 100 and check if the player has won. Should return False"""
        self.player1.add_score(15)
        has_won = self.game.check_if_won(self.player1)
        self.assertFalse(has_won) # Should return False as the score is below 100
        self.player1.add_score(37)
        has_won = self.game.check_if_won(self.player1)
        self.assertFalse(has_won) # Should still return False as the score is still below 100
        
    def test_checkIfWon(self):
        """Add 100 points to the player and check if the player has won. Should return True"""
        self.player1.add_score(100)
        has_won = self.game.check_if_won(self.player1)
        self.assertTrue(has_won) # Should return True as the score is now atleast 100 points
        self.player1.add_score(25) # Add another 25 points
        has_won = self.game.check_if_won(self.player1)
        self.assertTrue(has_won) # Should still return True as the score is still atleast 100 points
    
    def test_playerChoiceRoll(self):
        """Test the player_choice function with the input of roll"""
        self.assertTrue(self.game.player_choice(self.player1, "roll"))
        
    def test_playerChoiceHold(self):
        """Test the player_choice function with the input of hold"""
        self.assertTrue(self.game.player_choice(self.player1, "hold"))
        
    def test_playerChoiceQuit(self):
        """Test the player_choice function with the input of quit"""
        self.assertTrue(self.game.player_choice(self.player1, "quit"))
        
    def test_playerChoiceCheat(self):
        """Test the player_choice function with the input of cheat"""
        self.assertTrue(self.game.player_choice(self.player1, "cheat"))
    
    @patch("builtins.input", side_effect = ["Franklin"]) # An input is needed for the test
    def test_playerChoiceChangeName(self, fake_input):
        """Test the player_choice function with the input of changename"""
        self.assertTrue(self.game.player_choice(self.player1, "changename"))
        
    def test_playerChoiceCommands(self):
        """Test the player_choice function with the input of commands"""
        self.assertTrue(self.game.player_choice(self.player1, "commands"))
    
    @patch("builtins.input", side_effect = ["hold", "cheat"]) # An input is needed for the test
    def test_finishGamePVP(self, fake_input):
        """Test the player_vs_player function and attempt to finish a round"""
        self.assertTrue(True, self.game.player_versus_player(self.players))
        
    @patch("builtins.input", side_effect = ["cheat"]) # An input is needed for the test
    def test_finishGamePVPCheat(self, fake_input):
        """Test the player_vs_player function and attempt to finish a round with cheat"""
        self.assertTrue(True, self.game.player_versus_player(self.players))
        
    @patch("builtins.input", side_effect = ["hold", "cheat"]) # An input is needed for the test
    def test_finishGamePVC(self, fake_input):
        """Test the player_vs_player function and attempt to finish a round"""
        self.assertTrue(True, self.game.player_versus_computer(self.players))
        
if __name__ == "__main__":
    unittest.main()
    