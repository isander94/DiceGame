"""Main class for handling gameloop."""

import cmd
from game import Game
from player import Player
from highscore import Highscore


class GameLoop(cmd.Cmd):
    """Main Gameloop."""

    intro = "|¤¤¤¤| Pig Dice Game |¤¤¤¤|\nType 'help' to show commands."
    prompt = "--> "

    def do_menu(self, arg):
        """Show game menu."""
        print("\n" +
            "{    Option     }{    Command    }\n" +
            "|¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤||¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤|\n" +
            "|$ Singleplayer$||     pvc       |\n" +
            "|¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤||¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤|\n" +
            "|$ Multiplayer $||     pvp       |\n" +
            "|¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤||¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤|\n" +
            "| £ Highscore £ ||   highscore   |\n" +
            "|¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤||¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤|\n" +
            "|   € Rules €   ||     rules     |\n" +
            "|¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤||¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤|\n" +
            "|  :( Quit ):   ||     quit      |\n" +
            "|¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤|")

    def do_pvc(self, arg):
        """Start the game playing against the computer"""
        game = Game()
        print("Player vs Computer mode started!")
        low = 1
        high = 6
        cpu_high = 0
        players = []
        
        # Enter name and add to player list
        name = input(f"Enter name: ")
        players.append(Player(name, low, high))
        
        # Enter difficulty and add computer player to player list
        difficulty = int(input("Choose difficulty\n" +
                      "1) Normal\n" +
                      "2) Medium\n" +
                      "3) Hard\n" +
                      "4) Very hard!\n" +
                      "---> "
                      ))
        
        if difficulty == 1:
            cpu_high = 6
        elif difficulty == 2:
            cpu_high = 12
        elif difficulty == 3:
            cpu_high = 24
        elif difficulty == 4:
            cpu_high = 48
        
        players.append(Player("CPU", low, cpu_high))
        
        game.player_versus_computer(players)
        self.do_menu(arg)

    def do_pvp(self, arg):
        """Start the game with two players."""
        game = Game()
        print("Player versus Player mode started!")
        low = 1
        high = 6
        players = []
        
        for x in range (2):
            name = input(f"Enter name for player {x + 1}: ")
            players.append(Player(name, low, high))    
            
        game.player_versus_player(players)
        self.do_menu(arg)

    def do_highscore(self, arg):
        """Show highscore of previous played games."""
        highscore = Highscore()
        highscore.print_highscores()
        self.do_menu(arg)

    def do_rules(self, arg):
        """Display the rules of the game."""
        print(
            """\n
              Each turn a player gets to roll their dice as
              many times as they want, accumulating all points they get
              along the way. However if you roll a 1, you lose all your
              points you have gathered on that turn. Therefore it could be
              wise to hold on to your points after a few rolls.

              After the first player has either rolled a 1, or has decided to
              stay with their points, the turn goes over to the next player.

              This goes on until someone reaches 100 points first

              Good luck!""")

    def do_quit(self, line):
        """Quit the program."""
        return True


if __name__ == '__main__':
    GameLoop().cmdloop()
