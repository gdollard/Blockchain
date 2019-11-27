import datetime
import hashlib


# Author: G. Dollard
# Distributed Ledger Technology - Lab 1

# A class to represent a block in the blockchain
class Block:
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()
    block_reward = 20 # hardcode this value for now
    stake_placed = 0

    def __init__(self, data):
        self.data = data

    def get_next_block(self):
        return self.next;

    def set_next_block(self, nxt_block):
        self.next = nxt_block;

    def set_data(self, block_data):
        self.data = block_data;

    def set_previous_hash(self, hash):
        self.previous_hash = hash

    # used by the Casper Node
    def bet_stake(self, stake):
        self.stake_placed = stake

    # make a string of nonce, data, previous_hash and blockNo and return it as a gen_hash
    def gen_hash(self):
        the_hasher = hashlib.sha256()
        the_hasher.update(str(self.nonce).encode('utf-8'))
        the_hasher.update(self.data.encode('utf-8'))
        the_hasher.update(str(self.previous_hash).encode('utf-8'))
        the_hasher.update(str(self.blockNo).encode('utf-8'))
        the_hasher.update(str(self.timestamp).encode('utf-8'))
        return the_hasher.hexdigest()
