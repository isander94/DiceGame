"""Class for handling all game modes"""

from player import Player
from highscore import Highscore
import random

class Game:
    def __init__(self):
        """Initialize a game instance"""
        self.game_is_active = True
        self.round_score = 0
        
    def player_versus_player(self, players):
        """Method handling the game mode for two human players"""
        self.round_is_active = True
        self.show_commands()
        
        # Main game loop, continues until there is a winner or someone quits       
        while self.game_is_active:
            self.round_is_active = True
            # Alternate between the players
            if self.game_is_active:
                print(f"{players[0].get_name()}'s turn!")
            while self.round_is_active and self.game_is_active:
                move = input("---> ")
                self.player_choice(players[0], move)
                if self.check_if_won(players[0]):
                    self.game_is_active = False
                
            self.round_score = 0
            self.round_is_active = True
            
            if self.game_is_active:
                print(f"{players[1].get_name()}'s turn!")
            while self.round_is_active and self.game_is_active:
                move = input("---> ")
                self.player_choice(players[1], move)
                if self.check_if_won(players[1]):
                    self.game_is_active = False
                
        # Return true when the game is finished
        return True

    def player_versus_computer(self, players):
        """Method handling the game mode for player versus the computer"""
        """Method handling the game mode for two human players"""
        self.round_is_active = True
        self.show_commands()
        
        # Main game loop, continues until there is a winner or someone quits       
        while self.game_is_active:
            self.round_is_active = True
            # Alternate between the players
            if self.game_is_active:
                print(f"{players[0].get_name()}'s turn!")
            while self.round_is_active and self.game_is_active:
                move = input("---> ")
                self.player_choice(players[0], move)
                if self.check_if_won(players[0]):
                    self.game_is_active = False
                
            self.round_score = 0
            self.round_is_active = True
            
            if self.game_is_active:
                print(f"{players[1].get_name()}'s turn!")
            while self.round_is_active and self.game_is_active:
                # The computer either rolls the die or holds at random
                random_choice = random.randint(0, 100)
                move = "roll" if random_choice >= 50 else "hold"
                self.player_choice(players[1], move)
                if self.check_if_won(players[1]):
                    self.game_is_active = False
                
        # Return true when the game is finished
        return True

    def player_choice(self, player, choice):
        """Take a player object and a command and executes the corresponding game move"""
                    
        # Roll dice
        if choice.lower() == "roll":
            self.execute_roll(player)
            return True
                
        # Handle hold
        elif choice.lower() == "hold":
            player.add_score(self.round_score)
            self.round_is_active = False
            return True
            
        # Quit game session
        elif choice.lower() == "quit":
            self.game_is_active = False
            return True
            
        # Perform a cheat
        elif choice.lower() == "cheat":
            self.cheat(player)
            return True
            
        # Change name of the player
        elif choice.lower() == "changename":
            new_name = input("Enter new name: ")
            player.change_name(new_name)
            return True
            
        # Show game commands
        elif choice.lower() == "commands":
            self.show_commands()
            return True
            
    def execute_roll(self, player):
        """Rolls the player dice. If 1, the points are lost. If not, the points are added to the round"""
        roll = player.roll_dice()
        print(f"{player.get_name()} rolls {roll}!")
                
        # If the player rolls 1, the points for the round are lost
        if roll == 1:
            print(f"{player.get_name()} lost all points for this turn!")
            self.round_score = 0
            self.round_is_active = False
                    
        # If the player rolls above 1, the points are added to this rounds score
        else:
            self.round_score += roll
            print(f"{player.get_name()} now has {player.get_score() + self.round_score} points!")
        
    
    def check_if_won(self, player):
        """A simple function that checks if a player has won the game"""
        if player.get_score() >= 100:
            player.add_score(self.round_score)
            print(f"{player.get_name()} wins the game with a score of {player.get_score()}!")
            print(f"Game over!")
            # Add the player and score to the highscore list here
            highscore = Highscore()
            highscore.add_score(player.get_name(), player.get_score())
            return True
        return False
        
    def cheat(self, player):
        """A small function that adds 100 points to the player, thus ending the game with a victory"""
        player.add_score(100)

    def show_commands(self):
        """Shows availible commands for the game"""
        print("  Commands \n" +
                " ---------- \n" +
                "|   roll   |\n" +
                "|   hold   |\n" +
                "|   quit   |\n" +
                "|   cheat  |\n" +
                "|changename|\n" +
                " ---------- ")