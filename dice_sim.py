import operator
import random

class DiceSimulator:
    def __init__(self, num_dice=1, dice_size=6):
        self.dice = [i+1 for i in range(dice_size)]
        self.num_dice = num_dice


    def get_probability(self, success_operator=operator.eq, success_value=1, tries=1000000):

        successes = 0
        for _ in range(tries):
            total = 0
            for _ in range(self.num_dice):
                roll = random.choice(self.dice)
                total += roll
            if success_operator(total, success_value):
                successes += 1
        
        return successes / tries

    def set_dice_size(self, dice_size):
        self.dice_size = dice_size

    def set_num_dice(self, num_dice):
        self.num_dice = num_dice
