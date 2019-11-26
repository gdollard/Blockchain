from TendermintNode import TendermintNode
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
        node1 = TendermintNode(3)
        node2 = TendermintNode(5)
        node3 = TendermintNode(19)

        self.nodes = [node1, node2, node3]
        for node in self.nodes:
            node.register(self.nodes)

tendermint = Tendermint()
tendermint.initialise()
print("Nodes registered..")