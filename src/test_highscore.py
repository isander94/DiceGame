"""Unittest for highscore."""

import unittest
from highscore import Highscore


class TestHighscoreClass(unittest.TestCase):
    """Here the test for the highscore class happens."""

    def setUp(self):
        """Create a temporary test file."""
        self.test_file = "test_highscore.txt"
        try:
            with open(self.test_file, "r+"):
                pass
                # Check if file exists, if it does continue
            with open(self.test_file, "w") as f:
                f.write("")  # Empties the file
        except FileNotFoundError:
            pass
        self.test_highscore = Highscore(filename=self.test_file)

    def tearDown(self):
        """Remove test file after tests are done."""
        try:
            with open(self.test_file, "r+"):
                pass
            with open(self.test_file, "w") as f:
                f.write("")
        except FileNotFoundError:
            pass

    def test_add_highscore(self):
        """Test the add_highscore function."""
        self.test_highscore.add_score("Galileo", 100)
        self.assertEqual(self.test_highscore.get_highscore("Galileo"), 100)

    def test_update_score(self):
        """Test so that highscore gets updated correctly."""
        self.test_highscore.add_score("Oden", 60)
        self.test_highscore.add_score("Oden", 30)
        # lower than 60 -> should not update
        self.assertEqual(self.test_highscore.get_highscore("Oden"), 60)
        self.test_highscore.add_score("Oden", 90)
        # Higher than 60 -> should update
        self.assertEqual(self.test_highscore.get_highscore("Oden"), 90)

    def test_highscores_sorted(self):
        """Test if list gets sorted correctly."""
        self.test_highscore.add_score("Adam", 25)
        self.test_highscore.add_score("Bob", 75)
        self.test_highscore.add_score("Caesar", 50)
        highscores = self.test_highscore.get_every_highscore()
        self.assertEqual(highscores[0], ("Bob", 75))
        self.assertEqual(highscores[1], ("Caesar", 50))
        self.assertEqual(highscores[2], ("Adam", 25))

    def test_save_load_score(self):
        """Test if new instance still has same values."""
        self.test_highscore.add_score("David", 70)
        new_test_highscore = Highscore(filename=self.test_file)
        self.assertEqual(new_test_highscore.get_highscore("David"), 70)

    def test_file_format(self):
        """Test if file has 'player,points' format."""
        self.test_highscore.add_score("Eric", 20)
        with open(self.test_file, "r") as f:
            content = f.read().strip()
        self.assertEqual(content, "Eric,20")


if __name__ == "__main__":
    unittest.main()
