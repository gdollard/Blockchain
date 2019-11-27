from Block import Block

# Author: Glenn Dollard
class TendermintNode:

    stake = 0
    peer_nodes = None
    state = None
    validated_count = 0
    prevoted_count = 0
    pre_committed_count = 0
    committed_count = 0
    validated_count_threshold = 1
    prevoted_count_threshold = 1
    pre_committed_count_threshold = 1
    node_id = None

    def __init__(self, stake_value, node_id):
        self.stake = stake_value
        self.peer_nodes = []
        self.state = ""
        self.node_id = node_id

    # this function registers all the peer nodes with this node
    def register(self, nodes):
        for node in nodes:
            if node != self:
                self.peer_nodes.append(node)


    def validate_block(self, block):
        self.state = "PREVOTE"
        self.debug("Block " + block.data + " is valid, moving into PREVOTE state and informing all peer nodes.")
        # lets pretend the block is valid
        for node in self.peer_nodes:
            node.record_validated()

    def pre_vote_block(self):
        if self.state != "PREVOTE":
            self.debug("Requested to pre_vote block but not in the PRE_VOTE state, rejecting.")
            return
        else:
            if self.validated_count >= self.validated_count_threshold:
                self.state = "PRECOMMIT"
                self.debug("Just PRE_VOTED the block, now in PRE_COMMIT state")
                for node in self.peer_nodes:
                    node.record_prevoted()
            else:
                self.debug("Requested to pre_vote block but don't satisfy the required threshold , rejecting.")

    def pre_commit_block(self):
        if self.state != "PRECOMMIT":
            self.debug("Requested to pre_commit block but not in the PRE_COMMIT state, rejecting.")
            return
        else:
            if self.prevoted_count >= self.prevoted_count_threshold:
                self.state = "COMMIT"
                self.debug("Just PRE_COMMITTED the block, now in COMMIT state")
                for node in self.peer_nodes:
                    node.record_precommited()
            else:
                self.debug("Requested to pre_commit block but don't satisfy the required threshold , rejecting.")

    def commit_block(self):
        if self.state != "COMMIT":
            self.debug("Requested to commit block but not in the COMMIT state, rejecting.")
        else:
            if self.pre_committed_count >= self.pre_committed_count_threshold:
                self.debug("Just COMMITTED the block")
                self.state = "COMMITTED"
                for node in self.peer_nodes:
                    node.record_committed()
            else:
                self.debug("Requested to commit block but don't satisfy the required threshold , rejecting.")

    def record_validated(self):
        self.validated_count += 1

    def record_prevoted(self):
        self.prevoted_count += 1

    def record_precommited(self):
        self.pre_committed_count += 1

    def record_committed(self):
        self.committed_count += 1

    def debug(self, message):
        print("[" + str(self.node_id) + "] " + message)

