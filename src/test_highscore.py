"""Unittest for highscore."""

import unittest
from unittest.mock import patch
from highscore import Highscore


class TestHighscoreClass(unittest.TestCase):
    """Here the test for the highscore class happens."""

    def setUp(self):
        """Create a temporary test file."""
        self.test_file = "test_highscore.txt"
        try:
            with open(self.test_file, "r+", encoding="utf-8"):
                pass
                # Check if file exists, if it does continue
            with open(self.test_file, "w", encoding="utf-8") as f:
                f.write("")  # Empties the file
        except FileNotFoundError:
            pass
        self.test_highscore = Highscore(filename=self.test_file)

    def tearDown(self):
        """Remove test file after tests are done."""
        try:
            with open(self.test_file, "r+", encoding="utf-8"):
                pass
            with open(self.test_file, "w", encoding="utf-8") as f:
                f.write("")
        except FileNotFoundError:
            pass

    def test_add_highscore(self):
        """Test the add_highscore function."""
        self.test_highscore.add_score("Galileo", 100)
        self.assertEqual(self.test_highscore.get_highscore("Galileo"), 100)
        self.test_highscore.add_score("Dylan", 10)
        self.assertEqual(self.test_highscore.get_highscore("Dylan"), 10)

    def test_add_negative_score(self):
        """Test adding negative scores."""
        self.test_highscore.add_score("Kalle", -10)
        self.assertEqual(self.test_highscore.get_highscore("Kalle"), -10)
        self.test_highscore.add_score("Peter", -40)
        self.assertEqual(self.test_highscore.get_highscore("Peter"), -40)

    def test_dont_update_score(self):
        """Test that new score won't replace old score."""
        self.test_highscore.add_score("Oden", 60)
        self.test_highscore.add_score("Oden", 30)
        # lower than 60 -> should not update
        self.assertEqual(self.test_highscore.get_highscore("Oden"), 60)

        self.test_highscore.add_score("Filip", 90)
        self.test_highscore.add_score("Filip", 45)
        self.assertEqual(self.test_highscore.get_highscore("Filip"), 90)

    def test_update_score(self):
        """Test that new added score will replace old score."""
        self.test_highscore.add_score("Ben", 60)
        self.test_highscore.add_score("Ben", 90)
        # Higher than 60 -> should update
        self.assertEqual(self.test_highscore.get_highscore("Ben"), 90)

        self.test_highscore.add_score("Phil", 20)
        self.test_highscore.add_score("Phil", 50)
        self.assertEqual(self.test_highscore.get_highscore("Phil"), 50)

    def test_highscores_sorted(self):
        """Test if list gets sorted correctly."""
        self.test_highscore.add_score("Adam", 25)
        self.test_highscore.add_score("Bob", 75)
        self.test_highscore.add_score("Caesar", 50)
        self.test_highscore.add_score("David", 20)
        self.test_highscore.add_score("Eric", 15)
        self.test_highscore.add_score("Felix", 10)
        highscores = self.test_highscore.get_every_highscore()
        self.assertEqual(highscores[0], ("Bob", 75))
        self.assertEqual(highscores[1], ("Caesar", 50))
        self.assertEqual(highscores[2], ("Adam", 25))
        self.assertEqual(highscores[3], ("David", 20))
        self.assertEqual(highscores[4], ("Eric", 15))
        self.assertEqual(highscores[5], ("Felix", 10))

    def test_save_load_score(self):
        """Test if new instance still has same values."""
        self.test_highscore.add_score("David", 70)
        self.test_highscore.add_score("Kyle", 23)
        new_test_highscore = Highscore(filename=self.test_file)
        self.assertEqual(new_test_highscore.get_highscore("David"), 70)
        self.assertEqual(new_test_highscore.get_highscore("Kyle"), 23)

    def test_file_format(self):
        """Test if file has 'player,points' format."""
        self.test_highscore.add_score("Eric", 20)
        with open(self.test_file, "r", encoding="utf-8") as f:
            content = f.read().strip()
        self.assertEqual(content, "Eric,20")

    def test_special_character_name(self):
        """Test saving and loading player with special characters."""
        self.test_highscore.add_score("Örjan#1", 45)
        new_test_highscore = Highscore(filename=self.test_file)
        self.assertEqual(new_test_highscore.get_highscore("Örjan#1"), 45)

    @patch("builtins.print")
    def test_print_highscore_list(self, mock_print):
        """Test if printing highscores gives a fancy list."""
        self.test_highscore.add_score("Adam", 80)
        self.test_highscore.add_score("Bertil", 50)
        self.test_highscore.add_score("Caesar", 85)

        self.test_highscore.print_highscores()

        expected_output = [
            unittest.mock.call("\n¤¤ Highscore List ¤¤"),
            unittest.mock.call("1. Caesar - 85"),
            unittest.mock.call("2. Adam - 80"),
            unittest.mock.call("3. Bertil - 50"),
        ]

        mock_print.assert_has_calls(expected_output, any_order=False)

    @patch("builtins.print")
    def test_print_empty_highscore_list(self, mock_print):
        """Test that empty highscore list only prints the header."""
        self.test_highscore.print_highscores()
        mock_print.assert_called_once_with("\n¤¤ Highscore List ¤¤")


if __name__ == "__main__":
    unittest.main()
