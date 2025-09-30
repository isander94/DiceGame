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
        self.test_highscore.add_score("Oden", 60)
        self.test_highscore.add_score("Oden", 30)  # lower than 60 -> should not update
        self.assertEqual(self.test_highscore.get_highscore("Oden"), 60)
        self.test_highscore.add_score("Oden", 90)  # Higher than 60 -> should update
        self.assertEqual(self.test_highscore.get_highscore("Oden"), 90)
    
if __name__ == "__main__":
    unittest.main()
