

# This class represents a node for the Casper mining.
# Author: Glenn Dollard

class CasperNode:
    stake = 0;

    def __init__(self, stake, id):
        self.stake = stake

    # offer half the stake
    def get_stake_to_bet(self):
        return self.stake /2
