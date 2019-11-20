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
    timestamp = None

    def __init__(self, data):
        self.data = data
        self.timestamp = datetime.datetime.now()
        self.set_hash()

    def get_next_block(self):
        return self.next;

    def set_next_block(self, nxt_block):
        self.next = nxt_block;

    def get_data(self):
        return self.data

    def set_data(self, block_data):
        self.data = block_data;

    def set_previous_hash(self, hash):
        self.previous_hash = hash

    def get_previous_hash(self):
        return self.previous_hash

    def get_block_no(self):
        return self.blockNo

    def get_creation_date(self):
        return self.timestamp

    # make a string of nonce, data, previous_hash and blockNo and return it as a hash
    def set_hash(self):
        the_hasher = hashlib.sha256()
        the_hasher.update(self.data.encode('utf-8'))
        the_hasher.update(str(self.blockNo).encode('utf-8'))
        the_hasher.update(str(self.timestamp).encode('utf-8'))
        self.hash = the_hasher.hexdigest()

    def get_hash(self):
        return self.hash
