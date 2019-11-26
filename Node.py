import random


# This class represents a node which is used in the Ouroboros PoS algorithm
# Author: Glenn Dollard
class Node:
    stake = 0;

    def __init__(self, stake_value):
        self.stake = stake_value

    # the purpose of this is to randomly generate a number and keep going until all nodes produce the same number
    def coin_toss(self):
        # increase this range to increase the difficulty of forming a common coin toss across all nodes
        return random.randrange(1, 5)
