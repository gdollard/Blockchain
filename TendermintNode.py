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
    node_id = None
    leader = None
    committed_peers = []

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

    def validate_block(self, block, leader):
        self.leader = leader
        self.state = "PREVOTE"
        self.debug("Block " + block.data + " is valid, moving into PREVOTE state and informing all peer nodes.")
        # lets pretend the block is valid
        # include yourself as a validator
        self.record_validated()
        for node in self.peer_nodes:
            node.record_validated()

    def pre_vote_block(self):
        if self.state != "PREVOTE":
            self.debug("Requested to pre_vote block but not in the PRE_VOTE state, rejecting.")
            return
        else:
            if self.validated_count >= self.get_node_approval_threshold():
                self.state = "PRECOMMIT"
                self.debug("Just PRE_VOTED the block, now in PRE_COMMIT state")
                self.record_prevoted()
                for node in self.peer_nodes:
                    node.record_prevoted()
            else:
                self.debug("Requested to pre_vote block but don't satisfy the required threshold, rejecting.")

    def pre_commit_block(self):
        if self.state != "PRECOMMIT":
            self.debug("Requested to pre_commit block but not in the PRE_COMMIT state, rejecting.")
            return
        else:
            if self.prevoted_count >= self.get_node_approval_threshold():
                self.state = "COMMIT"
                self.debug("Just PRE_COMMITTED the block, now in COMMIT state")
                self.record_precommited()
                for node in self.peer_nodes:
                    node.record_precommited()
            else:
                self.debug("Requested to pre_commit block but don't satisfy the required threshold , rejecting.")

    def commit_block(self):
        if self.state != "COMMIT":
            self.debug("Requested to commit block but not in the COMMIT state, rejecting.")
        else:
            if self.pre_committed_count >= self.get_node_approval_threshold():
                self.debug("Just COMMITTED the block")
                self.state = "COMMITTED"
                self.record_committed()
                # tell the leader I have committed
                self.leader.inform_of_commit(self)
                for node in self.peer_nodes:
                    node.record_committed()
            else:
                self.debug("Requested to commit block but don't satisfy the required threshold , rejecting.")

    # this function will be called on the leader to register the committer node
    def inform_of_commit(self, committer_node):
        if self.state == "FINISHED":
            return
        if self.leader == self:
            self.committed_peers.append(committer_node)

    # moves the node into FINISHED state and resets the state counters
    def finish(self):
        self.state = "FINISHED"
        self.validated_count = 0
        self.prevoted_count = 0
        self.pre_committed_count = 0
        self.committed_count = 0

    def record_validated(self):
        self.validated_count += 1

    def record_prevoted(self):
        self.prevoted_count += 1

    def record_precommited(self):
        self.pre_committed_count += 1

    def record_committed(self):
        self.committed_count += 1

    # BFT states we can handle mining if we have at least two thirds good nodes
    def get_node_approval_threshold(self):
        total = len(self.peer_nodes) + 1
        #return round(len(self.peer_nodes) * .66)
        return round(total * .66)

    # This function marks the end of the rounds, it will be up to the leader to judge the result based on the voting states
    # and the voter count.
    def should_block_be_added(self):
        add_block = False
        if self.leader == self:
            total_peers = len(self.peer_nodes)+1
            ratio = len(self.committed_peers) / total_peers >= .66
            if ratio:
                add_block = True
                self.debug(
                    "Comitter here, we have enough commits (" + str(
                        len(self.committed_peers)) + " from a total of " + str(total_peers) + " peer nodes) to add the block, broadcasting FINISHED state to all nodes.")
            else:
                add_block = False
                self.debug(
                    "Comitter here, we DO NOT have enough commits (" + str(
                        len(self.committed_peers)) + " from a total of " + str(total_peers) + " peer nodes) to add the block, broadcasting FINISHED state to all nodes.")
        self.finish()
        for node in self.peer_nodes:
            node.finish()
        return add_block


    # Handy debugging to show the node ID
    def debug(self, message):
        print("[" + str(self.node_id) + "] " + message)
