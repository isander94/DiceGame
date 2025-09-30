"""Class for handling all game modes"""

from src.player import Player

class Game:
    def __init__(self):
        """Initialize a game instance"""
        self.game_is_active = True

    def player_versus_player(self):
        """Method handling the game mode for two human players"""
        print("Player versus Player mode started!")

        # The two players shall have a die with 6 faces
        low = 1
        high = 6

        # Ask the two players to enter their name and create player objects
        name = input("Player 1, please enter your name: ")
        player1 = Player(name, low, high)
        
        name = input("Player 2, please enter your name: ")
        player2 = Player(name, low, high)

        print(f"Welcome {player1.get_name()} and {player2.get_name()} - Prepare to roll!")

        # Enter a loop that alternates the control between player 1 and player 2
        while self.game_is_active:
            if self.game_is_active:            
                self.player_choice(player1)
                if self.check_if_won(player1):
                    self.game_is_active = False
            
            if self.game_is_active:
                self.player_choice(player2)
                if self.check_if_won(player2):
                    self.game_is_active = False

    def player_choice(self, player):
        """Reads the player input and executes the corresponding command"""
        round_score = 0
        round_is_active = True
        
        print(f"{player.get_name()}'s turn!")
        
        while round_is_active:
            player_input = input("--> ")
            
            # Roll
            if player_input.lower() == "roll":
                roll = player.roll_dice()
                print(f"{player.get_name()} rolls {roll}!")
                
                # If the player rolls 1, the points for the round are lost
                if roll == 1:
                    print(f"{player.get_name()} lost all points for this turn!")
                    round_score = 0
                    round_is_active = False
                    
                # If the player rolls above 1, the points are added to this rounds score
                else:
                    round_score += roll
                    print(f"{player.get_name()} now has {player.get_score() + round_score} points!")

            # Hold
            if player_input.lower() == "hold":
                # Add the round score to the player object - These points are now kept
                player.add_score(round_score)
                print(f"{player.get_name()} has secured {player.get_score()} points!")
                round_score = 0
                round_is_active = False
                
            # Quit
            # Cheat
            if player_input.lower() == "cheat":
                self.cheat(player)
                round_is_active = False
            # Change name
            # Show commands
            
    def check_if_won(self, player):
        if player.get_score() >= 100:
            print(f"{player.get_name()} wins the game with a score of {player.get_score()}!")
            print(f"Game over!")
            # Add the player and score to the highscore list here
            return True
        
    def cheat(self, player):
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