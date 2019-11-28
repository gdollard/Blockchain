

# This class represents a node for the Casper mining.
# Author: Glenn Dollard

class CasperNode:
    stake = 0;
    peer_nodes = None
    state = None
    prepared_count = 0
    committed_count = 0
    committed_peers = []
    leader = None
    block_to_add = None
    node_id = None

    def __init__(self, stake, id):
        self.stake = stake
        self.node_id = id
        self.peer_nodes = []

    # offer half the stake
    def get_stake_to_bet(self):
        return self.stake /2

    def register(self, nodes):
        for node in nodes:
            if node != self:
                self.peer_nodes.append(node)

    # Step 1 of 2 in the Casper algorithm
    def prepare(self, block, leader):
        self.leader = leader
        self.block_to_add = block
        # do some validation here...
        if self.validate_block():
            self.state = "PREPARED"
            self.record_prepared()
        for node in self.peer_nodes:
            node.record_prepared()

    def commit(self):
        if self.state == "PREPARED":
            if self.validate_block():
                if self.prepared_count >= self.get_node_approval_threshold():
                    self.state = "COMMITTED"
                    self.record_committed()
                    # tell the leader that I have committed
                    self.leader.inform_of_commit(self)
                    for node in self.peer_nodes:
                        node.record_committed()
                else:
                    self.debug("Requested to commit block but don't satisfy the required threshold , rejecting.")


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
                self.collect_reward()
            else:
                add_block = False
                self.debug(
                    "Comitter here, we DO NOT have enough commits (" + str(
                        len(self.committed_peers)) + " from a total of " + str(total_peers) + " peer nodes) to add the block, broadcasting FINISHED state to all nodes.")
        self.finish()
        for node in self.peer_nodes:
            node.finish()
        return add_block

    # moves the node into FINISHED state and resets the state counters
    def finish(self):
        self.state = "FINISHED"
        self.prepared_count = 0
        self.committed_count = 0
        self.committed_peers.clear()


    def get_node_approval_threshold(self):
        total = len(self.peer_nodes) + 1
        return round(total * .66)

    def validate_block(self):
        # do some mock validation here
        return True

    def record_prepared(self):
        self.prepared_count += 1

    def record_committed(self):
        self.committed_count += 1

    def inform_of_commit(self, committer_node):
        if self.state == "FINISHED":
            return
        if self.leader == self:
            self.committed_peers.append(committer_node)

    # if the consensus to add the block has been reached then the leader can collect the fee
    # the fee is weighted on the stake placed.
    def collect_reward(self):
        if self.leader == self:
            stake_weighting = self.block_to_add.stake_placed / 2
            self.stake += self.block_to_add.block_reward * stake_weighting
            print("Yippee, I earned an award, stake is now: ", self.stake)


    # Handy debugging to show the node ID
    def debug(self, message):
        print("Casper::[" + str(self.node_id) + "] " + message)