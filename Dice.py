import random


class Dice():

    def __init__(self, min, max):
        self.min = min
        self.max = max

    def roll(self):
        result = random.randint(self.min, self.max)
        return result
