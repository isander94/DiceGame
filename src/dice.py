"""Class representing a die that can be rolled."""

import random


class Dice:
    """Create a dice class with a low and high value."""

    def __init__(self, low, high):
        """Initialize with low and high number."""
        self.low = low
        self.high = high

    def roll(self):
        """Roll the dice, returning a number between low and high."""
        random_num = random.randint(self.low, self.high)
        return random_num
