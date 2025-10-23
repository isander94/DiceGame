"""Class representing a die that can be rolled."""
# pylint: disable=too-few-public-methods
import random


class Dice:
    """Create a dice class with a low and high value."""

    def __init__(self, low, high):
        """Initialize with low and high number."""
        # Makes sure dice low and high can only be Integer
        if not isinstance(low, int) or not isinstance(high, int):
            raise TypeError("Low and high values must be integers.")

        # Makes sure a dice cant have low > high
        if low > high:
            raise ValueError("Low cannot be greater than high.")

        self.low = low
        self.high = high

    def roll(self):
        """Roll the dice, returning a number between low and high."""
        random_num = random.randint(self.low, self.high)
        return random_num
