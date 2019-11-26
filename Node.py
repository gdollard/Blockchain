import random

# This class represents a node which is used in the Ouroboros PoS algorithm
# Author: Glenn Dollard
class Node:
    stake = 0;

    def __init__(self, stake_value):
        self.stake = stake_value

    # the purpose of this is to randomly generate a number and keep going until all nodes produce the same number
    def coin_toss(self, random_maximum):
        # increase this range to increase the difficulty of forming a common coin toss across all nodes
        return random.randrange(1, 5)

    def gen_rand(self):
        return random.randrange(0, 4)

    #resume: make this random range narrow because we may have a large number of nodes. Problem is then though using this
    #random number to link back to somehow contribute to deriving a random selection across the entire stake count.

