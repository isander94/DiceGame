"""Highscore file."""


class Highscore:
    """Highscore class."""

    def __init__(self, filename="highscore.txt"):
        """Highscore init."""
        self.filename = filename
        self.highscores = {}
        self.load_scores()

    def add_score(self, player, score):
        """Add or update a players score."""
        if player not in self.highscores or score > self.highscores[player]:
            self.highscores[player] = score
            self.save_scores()
        else:
            pass  # No new player score or better than previous

    def get_highscore(self, player):
        """Return players highscore, if doesn't exist return 0."""
        return self.highscores.get(player, 0)

    def get_every_highscore(self):
        """Return a sorted highscore list in falling order."""
        return sorted(
            self.highscores.items(), key=lambda x: x[1], reverse=True)

    def print_highscores(self):
        """Print the highscores in a fancy list."""
        print("\n¤¤ Highscore List ¤¤")
        for i, (player, score) in enumerate(
                self.get_every_highscore(), start=1):
            print(f"{i}. {player} - {score}")

    def save_scores(self):
        """Save the highscore."""
        with open(self.filename, "w") as f:
            for player, score in self.highscores.items():
                f.write(f"{player},{score}\n")

    def load_scores(self):
        """Load previous highscores."""
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    player, score = line.strip().split(",")
                    self.highscores[player] = int(score)
        except FileNotFoundError:
            pass  # If file doesn't exist ignore
