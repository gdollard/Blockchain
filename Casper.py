from CasperNode import CasperNode
import random
# each block will bet against a block using its stake. If they are selected to add the block they will
# earn a reward proportional to their stake.

# if however they are seen to misbehave their stake is slashed

# Author: Glenn Dollard

class Casper:
    stake = 0;

    nodes = []

    def bootstrap(self):
        num_nodes = input("Enter the number of Nodes: ")
        try:
            num_nodes = int(num_nodes)
        except ValueError:
            print("Invalid argument supplied, quitting.")
            # quit the program if we have invalid data
            exit()
        for counter in range(num_nodes):
            new_node = CasperNode(random.randrange(1, 101), "ouroboros_node_" + str(counter))
            self.nodes.append(new_node)

        for node in self.nodes:
            node.register(self.nodes)

    def get_tickets_for_nodes(self):
        tickets = []
        for node in self.nodes:
            for index in range(node.stake):
                tickets.append(node.id)
        return tickets

    # Kicks off the proposal
    def begin(self, block):

        # select the leader, this leader will be the one determining whether to add the block or not
        # Pick a proposer weighted on their stake
        leader = random.randrange(len(self.get_tickets_for_nodes))
        block.bet_stake(leader.get_stake_to_bet())
        # first commit the stake to the height, give the block a height

        # implement the functions below in the Casper Node

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
        # if should be added then reward the leader with a fee proportional to their stake
        return leader.should_block_be_added()


