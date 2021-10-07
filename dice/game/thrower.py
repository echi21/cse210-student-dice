import random

class Thrower:
    """A code template for a person who plays the game. The responsibility of 
    this class of objects is to determine if it can throw the dices, calculate the points
    in the game according to the rules, and throw the dices geting the points for each turn. 
    
    Attributes:
        dice (list): Stores the numbers that exist in a dice from 1 to 6.
    """

    def __init__(self):
        """The constructor declares and initializes instance attributes with their default values.

        Args:
            self (Thrower): an instance of Thrower.
        """
        self.dice = []
        self.total = 0

    def throw_dice(self):
        """Generates five new dice values and adds them to the dice list.

        Args:
            self (Thrower): An instance of Thrower.
        """
        for _ in range(5):
            dice_value = random.randint(1,6)
            self.dice.append(dice_value)

    def get_points(self):
        """Calculates the total number of points for the current dice. Ones are worth 100 points.
        Fives are worth 50 points.

        Args:
            self (Thrower): An instance of Thrower.
        Returns:
            self.total: The total points for the current throw.
        """
        self.total = 0
        for i in self.dice:
            if i == 1:
                self.total += 100
            elif i == 5:
                self.total += 50
        return self.total

    def can_throw(self):
        """Determines whether or not the Thrower can throw again.
        
        Args:
            self (Thrower): An instance of Thrower.
        Returns:
            boolean: True if the list of dice has at least a five, or a one. Otherwise, it returns false.
        """
        if (1 in self.dice) or (5 in self.dice):
            self.dice.clear()
            return True
        else:
            print("The game is over! Good luck next time!")
            return False