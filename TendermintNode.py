from Block import Block

# Author: Glenn Dollard
class TendermintNode:

    stake = 0
    peer_nodes = None
    state = None
    pre_vote_count = 0
    pre_commit_count = 0
    commit_count = 0
    validated_count = 0
    prevoted_count = 0
    pre_committed_count = 0
    committed_count = 0

    def __init__(self, stake_value):
        self.stake = stake_value
        self.peer_nodes = []
        self.state = ""

    # this function registers all the peer nodes with this node
    def register(self, nodes):
        for node in nodes:
            if node != self:
                self.peer_nodes.append(node)

    def propose(self, block):
        print("In propose, validating the block")
        print("Proposer: Block is valid, entering prevote")
        self.state = "PREVOTE"
        self.pre_vote_count += 1
        #broadcasting
        for node in self.peer_nodes:
            node.pre_vote()
            node.validate_block(block)



    def validate_block(self, block):
        print("Validating this block: " + block.data + ", OK, it's valid, entering PREVOTE State")
        self.state = "PREVOTE"
        #self.pre_vote_count += 1
        # lets pretend the block is valid
        for node in self.peer_nodes:
            node.record_validated()
            #node.pre_vote()

    def pre_vote_block(self):
        if self.state != "PREVOTE":
            return
        else:
            if self.validated_count >= 1:
                self.state = "PRECOMMIT"
                print("Just PRE_VOTED the block, now in PRE_COMMIT state")
                for node in self.peer_nodes:
                    node.record_prevoted()

    def pre_commit_block(self):
        if self.state != "PRECOMMIT":
            return
        else:
            if self.prevoted_count >=1:
                self.state = "COMMIT"
                print("Just PRE_COMMITTED the block, now in COMMIT state")
                for node in self.peer_nodes:
                    node.record_precommited()

    def commit_block(self):
        if self.state == "COMMIT":
            if self.pre_committed_count >=1:
                print("Just COMMITTED the block")
                self.state = "COMMITTED"
                for node in self.peer_nodes:
                    node.record_committed()



    def record_validated(self):
        self.validated_count += 1

    def record_prevoted(self):
        self.prevoted_count += 1

    def record_precommited(self):
        self.pre_committed_count += 1

    def record_committed(self):
        self.committed_count += 1

