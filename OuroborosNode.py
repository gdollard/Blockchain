import random

# See Ref: https://cardanodocs.com/cardano/proof-of-stake/

# This class represents a node which is used in the Ouroboros PoS algorithm.
# As part of the Multiparty Computation each node is tasked with tossing a coin.
# This class contains the implementation for tossing the coin.
# Author: Glenn Dollard
class OuroborosNode:
    stake = 0;

    def __init__(self, stake_value):
        self.stake = stake_value

    # the purpose of this is to randomly generate a number and keep going until all nodes produce the same number
    def coin_toss(self):
        # increase this range to increase the difficulty of forming a common coin toss across all nodes
        return random.randrange(1, 5)
