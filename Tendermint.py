from TendermintNode import TendermintNode
from Block import Block
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

        # select the

        # let the first node propose (for now)
        self.nodes[0].validate_block(block)
        self.nodes[1].validate_block(block)

        self.nodes[0].pre_vote_block()
        self.nodes[1].pre_vote_block()

        self.nodes[0].pre_commit_block()
        self.nodes[1].pre_commit_block()

        self.nodes[0].commit_block()
        self.nodes[1].commit_block()


tendermint = Tendermint()
tendermint.initialise()
tendermint.begin()