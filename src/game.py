"""Class for handling all game modes."""

# pylint: disable=attribute-defined-outside-init
# pylint: disable=too-many-return-statements
import random
from highscore import Highscore


class Game:
    """Class handling the two game modes and their corresponding logic."""

    def __init__(self):
        """Initialize a game instance."""
        self.game_is_active = True
        self.round_score = 0

    def player_versus_player(self, players):
        """Handle the game mode for two human players."""
        self.round_is_active = True
        self.show_commands()

        # Main game loop, continues until there is a winner or someone quits
        while self.game_is_active:
            self.round_score = 0
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
        """Handle the game mode for player versus the computer."""
        self.round_is_active = True
        self.show_commands()

        # Main game loop, continues until there is a winner or someone quits
        while self.game_is_active:
            self.round_score = 0
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
        """Execute the corresponding command depending on player input."""
        # Roll dice
        if choice.lower() == "roll":
            self.execute_roll(player)
            return True

        # Handle hold
        if choice.lower() == "hold":
            print(f"{player.get_name()} holds!")
            player.add_score(self.round_score)
            self.round_is_active = False
            return True

        # Quit game session
        if choice.lower() == "quit":
            self.game_is_active = False
            return True

        # Perform a cheat
        if choice.lower() == "cheat":
            self.cheat(player)
            return True

        # Change name of the player
        if choice.lower() == "changename":
            new_name = input("Enter new name: ")
            player.change_name(new_name)
            return True

        # Show game commands
        if choice.lower() == "commands":
            self.show_commands()
            return True

        return True

    def execute_roll(self, player):
        """Roll the player dice."""
        roll = player.roll_dice()
        print(f"{player.get_name()} rolls {roll}!")

        # If the player rolls 1, the points for the round are lost
        if roll == 1:
            print(f"{player.get_name()} lost all points for this turn!")
            self.round_score = 0
            self.round_is_active = False

        # If the player rolls over 1, the points are added to this rounds score
        else:
            self.round_score += roll
            print(
                f"{player.get_name()} now has "
                f"{player.get_score() + self.round_score} points!"
            )

    def check_if_won(self, player):
        """Check if a player has won the game."""
        if player.get_score() >= 100:
            print(
                f"{player.get_name()} wins the game "
                f"with a score of {player.get_score()}!"
            )
            print("Game over!")
            # Add the player and score to the highscore list here
            highscore = Highscore()
            highscore.add_score(player.get_name(), player.get_score())
            return True
        return False

    def cheat(self, player):
        """Add 100 points to the player, ending the game with a victory."""
        player.add_score(100)

    def show_commands(self):
        """Show the availible commands for the game."""
        print(
            "  Commands \n"
            + " ---------- \n"
            + "|   roll   |\n"
            + "|   hold   |\n"
            + "|   quit   |\n"
            + "|   cheat  |\n"
            + "|changename|\n"
            + " ---------- "
        )
