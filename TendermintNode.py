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
                for node in self.peer_nodes:
                    node.record_prevoted()

    def pre_commit_block(self):
        if self.state != "PRECOMMIT":
            return
        else:
            if self.prevoted_count >=1:
                self.state = "COMMIT"
                for node in self.peer_nodes:
                    node.record_prevoted()

    def commit_block(self):




    def pre_vote(self):
        self.pre_vote_count += 1  # record the fact that some other node is ready to vote
        if self.state == "PREVOTE":
            # I am in prevote state so I'm listening
            if self.pre_vote_count >=2: ##hard code this for now, obviously will need to base it on 2/3
                print("Pre-vote has passed, entering PRECOMMIT")
                self.state = "PRECOMMIT"
                self.pre_vote_count = 0
                # broadcast to all
                for node in self.peer_nodes:
                    node.pre_commit()

    def pre_commit(self):
        self.pre_commit_count += 1
        if self.state == "PRECOMMIT":
            if self.pre_commit_count >=2: ##hard code this for now, obviously will need to base it on 2/3
                print("Pre-vote has passed, entering PRECOMMIT")
                self.state = "COMMIT"
                self.pre_commit_count = 0
                # broadcast to all
                for node in self.peer_nodes:
                    node.commit()

    def commit(self):
        if self.state == "COMMIT":
            self.commit_count += 1
            if self.commit_count >=2: #hardcode this for now, obviously will need to base it on 2/3
                print("Pre-vote has passed, entering COMMIT")
                self.state = "COMMITTED"
                self.commit_count = 0
                # add the block
                print("Reached COMMITTED, add the block")


    def record_validated(self):
        self.validated_count += 1

    def record_prevoted(self):
        self.prevoted_count += 1

    def record_precommited(self):
        self.pre_committed_count += 1

