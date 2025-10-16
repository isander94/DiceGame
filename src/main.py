"""Main class for handling gameloop."""

import cmd
from game import Game
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
            "|   $ Play $    ||     play      |\n" +
            "|¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤||¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤|\n" +
            "| £ Highscore £ ||   highscore   |\n" +
            "|¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤||¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤|\n" +
            "|   € Rules €   ||     rules     |\n" +
            "|¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤||¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤|\n" +
            "|  :( Quit ):   ||     quit      |\n" +
            "|¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤|")

    def do_play(self, arg):
        """Start the game."""
        game = Game()
        game.player_versus_player()
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
