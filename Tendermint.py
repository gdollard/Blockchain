from TendermintNode import TendermintNode
from Block import Block
import random

# REF https://blockgeeks.com/guides/tendermint/
# REF https://tendermint.readthedocs.io/en/latest/introduction.html

# Author: Glenn Dollard
class Tendermint:

    nodes = []

    def bootstrap_tendermint(self):
        num_nodes = input("Enter the number of Nodes: ")
        try:
            num_nodes = int(num_nodes)
        except ValueError:
            print("Invalid argument supplied, quitting.")
            # quit the program if we have invalid data
            exit()
        for counter in range(num_nodes):
            new_node = TendermintNode(random.randrange(1, 101), "ouroboros_node_" + str(counter))
            self.nodes.append(new_node)

        for node in self.nodes:
            node.register(self.nodes)

    # Kicks off the proposal
    def begin(self, block):

        # select the leader, this leader will be the one determining whether to add the block or not
        # Pick a proposer weighted on their stake

        leader = self.nodes[random.randrange(0, len(self.nodes))]

        # let the first node propose (for now)
        for node in self.nodes:
            node.validate_block(block, leader)

        for node in self.nodes:
            node.pre_vote_block()

        for node in self.nodes:
            node.pre_commit_block()

        for node in self.nodes:
            node.commit_block()

        # simulated end-of-rounds, get the result from the leader
        return leader.should_block_be_added()