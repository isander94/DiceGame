"""Player class that represents a participant in the game"""
#from dice import Dice


class Player:
    def __init__(self, name):
        """Initialize a player object with a name as parameter"""
        self.name = name
        self.score = 0
        #self.dice = Dice(1, 6)

    def get_score(self):
        """Return the score of the player instance"""
        return self.score
    
    def add_score(self, score):
        """Add a score the player instance with score as a parameter"""
        self.score += score

    def get_name(self):
        """Return the name of the player instance"""
        return self.name
    
    def change_name(self, new_name):
        """Change the name of the player instance with new_name as a parameter"""
        self.name = new_name

