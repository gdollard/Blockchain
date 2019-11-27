from TendermintNode import TendermintNode
from Block import Block
import random
# Tendermint is a mostly asynchronous, deterministic, BFT consensus where validators
# have a stake which denotes their voting power.

# if more than a third of the validators are malicious, instead of the network forking, the Tendermint blockchain
# will simply come to a temporary halt until more 2 / 3rd validators come to a consensus.

# Tendermint is also completely deterministic and there is no randomness in the protocol.
# The leaders in the system are all elected in a deterministic version, via a defined mathematical function.

# When a block gets >2/3 of the prevotes at (H,R) then it is called proof-of-lock-change or PoLC.

#the states that each round goes through? NewHeight, Propose, Prevote, Precommit, and Commit.

# Number of validators grows under a controlled manner. Starts at 100 and will increase by 13% each year for 10 years
# when it will settle at 300.

# REF https://blockgeeks.com/guides/tendermint/
# REF https://tendermint.readthedocs.io/en/latest/introduction.html
class Tendermint:

    nodes = []

    def initialise(self):
        # create some nodes
        node1 = TendermintNode(3, 111)
        node2 = TendermintNode(5, 222)
        node3 = TendermintNode(19, 333)
        node4 = TendermintNode(21, 44)
        node5 = TendermintNode(67, 555)
        node6 = TendermintNode(8, 66)
        node7 = TendermintNode(119, 77)
        node8 = TendermintNode(695, 88)
        node9 = TendermintNode(12, 99)
        node10 = TendermintNode(3, 1010)


        self.nodes = [node1, node2, node3, node4, node5, node6, node7, node8, node9, node10]

        for node in self.nodes:
            node.register(self.nodes)

    # Kicks off the proposal
    def begin(self):
        block = Block('SampleTendermint Block')

        # select the leader, this leader will be the one determining whether to add the block or not
        #randomly pick for now
        leader = self.nodes[random.randrange(0, len(self.nodes))]

        # let the first node propose (for now)
        self.nodes[0].validate_block(block, leader)
        self.nodes[1].validate_block(block, leader)
        self.nodes[2].validate_block(block, leader)
        self.nodes[3].validate_block(block, leader)
        self.nodes[4].validate_block(block, leader)
        self.nodes[5].validate_block(block, leader)
        self.nodes[6].validate_block(block, leader)
        self.nodes[7].validate_block(block, leader)
        self.nodes[8].validate_block(block, leader)
        self.nodes[9].validate_block(block, leader)

        self.nodes[0].pre_vote_block()
        self.nodes[1].pre_vote_block()
        self.nodes[2].pre_vote_block()
        self.nodes[3].pre_vote_block()
        self.nodes[4].pre_vote_block()
        self.nodes[5].pre_vote_block()
        self.nodes[6].pre_vote_block()
        self.nodes[7].pre_vote_block()
        self.nodes[8].pre_vote_block()
        self.nodes[9].pre_vote_block()

        self.nodes[0].pre_commit_block()
        self.nodes[1].pre_commit_block()
        self.nodes[2].pre_commit_block()
        self.nodes[3].pre_commit_block()
        self.nodes[4].pre_commit_block()
        self.nodes[5].pre_commit_block()
        self.nodes[6].pre_commit_block()
        self.nodes[7].pre_commit_block()
        self.nodes[8].pre_commit_block()
        self.nodes[9].pre_commit_block()

        self.nodes[0].commit_block()
        self.nodes[1].commit_block()
        self.nodes[2].commit_block()
        self.nodes[3].commit_block()
        self.nodes[4].commit_block()
        self.nodes[5].commit_block()
        self.nodes[6].commit_block()
        self.nodes[7].commit_block()
        self.nodes[8].commit_block()
        self.nodes[9].commit_block()

        # simulated end-of-rounds, get the result from the leader
        should_add = leader.should_block_be_added()
        if should_add:
            print("Yes, add the block")
        else:
            print("Do Not add the block")


tendermint = Tendermint()
tendermint.initialise()
tendermint.begin()