import Block

# Author: Glenn Dollard
class TendermintNode:
    stake = 0
    peer_nodes = None

    def __init__(self, stake_value):
        self.stake = stake_value
        self.peer_nodes = []

    # this function registers all the peer nodes with this node
    def register(self, nodes):
        for node in nodes:
            if node != self:
                self.peer_nodes.append(node)


